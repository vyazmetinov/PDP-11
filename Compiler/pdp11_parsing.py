import pyparsing as pp
from typing import Dict, Optional, Union
import re

class Data:
    """
    Здесь мы определяем допустимые команды и регистры.
    """
    commands = {"mov", "add", "sub", "halt", "inc"}  # Набор допустимых команд
    registers = {f"R{x}" for x in range(8)} | {"SP", "PC"}  # Набор допустимых имен регистров (R0 - R7)
    register_aliases = {"SP": "R6", "PC": "R7"}

    @classmethod
    def is_valid_register(cls, reg):
        reg_upper = reg.upper()
        return reg_upper in cls.registers or reg_upper in cls.register_aliases


class PDP11Parser:
    def __init__(self):
        self.init_grammar()

    def init_grammar(self):
        # Базовые элементы
        identifier = pp.Word(pp.alphas + "_", pp.alphanums + "_")  # Идентификатор (метка, переменная)
        number = pp.Combine(
            pp.Optional(pp.oneOf("+ -")) + pp.Word(pp.nums)  # Обрабатывает числа со знаком
        ).addParseAction(lambda t: int(t[0]))  # Преобразует разобранное число в целое число

        reg = (
                pp.Combine(
                    pp.CaselessLiteral("R") + pp.Word(pp.nums)) |  # Соответствует именам регистров (например, R0, R1)
                pp.CaselessLiteral("SP") |
                pp.CaselessLiteral("PC")
        ).setParseAction(lambda t: t[0].upper())

        # Способы адресации
        immediate = pp.Combine("#" + (number | identifier))  # Непосредственное значение (например, #10, #метка)
        absolute = pp.Combine(
            "@" + pp.Optional("#") + (number | identifier))  # Абсолютный адрес (например, @1000, @#variable)
        reg_deferred = pp.Combine("(" + reg + ")") | pp.Combine(
            "@" + reg)  # Регистровая адресация (например, (R0), @R1)

        auto_inc_indirect = pp.Combine(
            "@" + pp.Optional(pp.White()) +
            "(" + pp.Optional(pp.White()) +
            reg +
            pp.Optional(pp.White()) + ")+"
        ).setParseAction(lambda t: '@' + t[0][1:].replace(" ", ""))

        auto_inc = pp.Combine(
            "(" + pp.Optional(pp.White()) +
            reg +
            pp.Optional(pp.White()) + ")+"
        ).setParseAction(lambda t: t[0].replace(" ", ""))  # Автоинкремент (например, (R0)+)

        auto_dec = pp.Combine(
            "-" + "(" + reg + ")"
        ).setParseAction(lambda t: t[0].replace(" ", ""))  # Автодекремент (например, -(R1))

        auto_dec_indirect = pp.Combine(
            "@-" + "(" + reg + ")"
        ).setParseAction(lambda t: t[0].replace(" ", ""))  # Косвенный автодекремент  @-(R1)

        indexed = pp.Combine(
            pp.Optional(number, default="0") +
            "(" + reg + ")" +
            pp.Optional("+", default="")
        )  # индексированная адресация

        parameter = (
                immediate |
                absolute |
                auto_inc_indirect |
                auto_inc |
                auto_dec_indirect |
                auto_dec |
                reg_deferred |
                indexed |
                reg |
                number
        )

        label = (identifier + pp.Suppress(":")).setResultsName("label",
                                                               listAllMatches=True)  # Метка (идентификатор, за которым следует двоеточие)
        command = pp.oneOf(list(Data.commands), caseless=True).setResultsName(
            "command")  # Команда (из списка допустимых команд)
        args = pp.Group(
            pp.Suppress(pp.Optional(',')) + parameter + pp.Suppress(",") + parameter
        ).setResultsName("args") | pp.Group(parameter).setResultsName("args")  # Аргументы команды
        comment = pp.Suppress(";") + pp.restOfLine.setResultsName("comment")  # Комментарий (начинается с ";")

        self.parser = pp.ZeroOrMore(label) + command + pp.Optional(args) + pp.Optional(comment)

    def parse(self, line):
        try:
            result = self.parser.parseString(line,
                                             parseAll=True).asDict()  # Разбирает строку и преобразует результаты в словарь
            self.post_process(result)  # Выполняет постобработку результатов
            self.validate(result)  # Выполняет валидацию результатов
            return result
        except pp.ParseException as e:
            return {"error": str(e)}

    def post_process(self, result):
        """
        Выполняет постобработку результатов разбора, например, нормализует регистры.
        """
        if 'label' in result:
            # Обработка меток
            if isinstance(result['label'], list):
                result['label'] = [item for sublist in result['label'] for item in sublist]

        if 'args' in result:  # Если в результате есть аргументы
            args = []
            for arg in result['args']:
                if isinstance(arg, list):
                    processed = arg[0]
                else:
                    processed = ''.join(str(arg).split())

                processed = Data.register_aliases.get(processed.upper(), processed)
                if processed.upper().startswith('R'):
                    processed = processed.upper()
                args.append(processed)
            result['args'] = args

    def validate(self, result):
        """
        Выполняет корректность результатов разбора
        """
        if 'args' in result:
            for arg in result['args']:
                if isinstance(arg, str) and arg.upper() in {'R8', 'R9', 'r8', 'r9'}:
                    raise ValueError("Недопустимый регистр (допустимы R0-R7)")

        if 'command' not in result:
            raise ValueError("Отсутствует команда")

        cmd = result['command'].lower()  # Получаем команду в нижнем регистре
        if cmd in {'mov', 'add', 'sub'} and len(result.get('args', [])) != 2:
            raise ValueError(f"Команда {cmd} требует 2 аргумента")
        elif cmd == 'inc' and len(result.get('args', [])) != 1:
            raise ValueError("Команда inc требует 1 аргумента")

    @staticmethod
    def parse_arg(arg_str: str) -> Dict[str, Optional[Union[int, str]]]:
        """
        Парсит аргумент командыи возвращает режим адресации, номер регистра и дополнительное значение.
        """
        arg = arg_str.strip().upper()
        result = {"mode": 0, "regnum": None, "additional_value": None}

        # 1. Проверка на регистр (R0-R7, PC, SP)
        if arg in Data.registers:
            result["regnum"] = 6 if arg == "SP" else (7 if arg == "PC" else int(arg[1]))
            return result

        # 2. Проверка на числа (#123, @123, 123, -123)
        if (num_match := re.match(r"^[@#]?(-?\d+)$", arg)):
            num = int(num_match.group(1))
            result["mode"] = 27 if arg.startswith("#") else 37
            result["additional_value"] = num
            return result

        # 3. Проверка сложных режимов адресации (X(Rn), @(Rn)+, -(Rn), и т.д.)
        complex_patterns = {
            r"^@\((R[0-7]|PC|SP)\)\+$": {"mode": 3, "reg_group": 1},
            r"^\((R[0-7]|PC|SP)\)\+$": {"mode": 2, "reg_group": 1},
            r"^@-\((R[0-7]|PC|SP)\)$": {"mode": 5, "reg_group": 1},
            r"^-\((R[0-7]|PC|SP)\)$": {"mode": 4, "reg_group": 1},
            r"^@\((R[0-7]|PC|SP)\)$": {"mode": 1, "reg_group": 1},
            r"^\((R[0-7]|PC|SP)\)$": {"mode": 1, "reg_group": 1},
            r"^@?(-?\d+)\((R[0-7]|PC|SP)\)$": {"mode": lambda m: 7 if m.group(0).startswith("@") else 6, "reg_group": 2,
                                               "value_group": 1},
        }

        for pattern, config in complex_patterns.items():
            if match := re.fullmatch(pattern, arg):
                reg = match.group(config["reg_group"])
                result["regnum"] = 6 if reg == "SP" else (7 if reg == "PC" else int(reg[1]))

                if "value_group" in config:
                    result["additional_value"] = int(match.group(config["value_group"]))

                if callable(config["mode"]):
                    result["mode"] = config["mode"](match)
                else:
                    result["mode"] = config["mode"]

                return result

        return result
    def compile(self, source_lines: list[str]) -> list[dict]:
        """
        Компилирует список строк ассемблерного кода в список словарей с разобранными данными.
        Каждый словарь содержит:
        - 'adr': адрес в памяти (в восьмеричном формате)
        - 'label': название метки (если есть)
        - 'cmd': полная команда с аргументами
        - 'comment': комментарий (если есть)
        - 'parsed': разобранные данные команды
        """
        compiled = []
        current_address = 0o1000  # Начальный адрес (восьмеричный)

        for line in source_lines:
            line = line.strip()
            if not line:  # Пропускаем пустые строки
                continue

            # Разбираем строку
            parsed = self.parse(line)
            if "error" in parsed:
                continue  # или можно выкидывать исключение

            # Формируем запись
            entry = {
                'adr': f"{current_address:06o}",  # Адрес в 6-значном восьмеричном формате
                'label': parsed.get('label', [''])[0] if 'label' in parsed else '',
                'cmd': line.split(';')[0].strip(),  # Вся команда до комментария
                'comment': parsed.get('comment', ''),
                'parsed': parsed
            }

            compiled.append(entry)

            # Обновляем адрес (каждая команда занимает 2 байта)
            current_address += 2

            # Если команда имеет аргументы, увеличиваем адрес дополнительно
            if 'args' in parsed and parsed['args']:
                # Простейшая эвристика: каждый аргумент добавляет 2 байта
                current_address += len(parsed['args']) * 2

        return compiled

source = [
    "main: mov #123, R1 ; Инициализация",
    "loop: add R1, R2",
    "      sub #1, R1",
    "      bne loop",
    "      halt"
]

parser = PDP11Parser()
compiled = parser.compile(source)

for entry in compiled:
    print(f"Разобранные данные: {entry['parsed']}")
    print("-" * 40)