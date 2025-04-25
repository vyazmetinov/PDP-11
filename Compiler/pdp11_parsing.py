import pyparsing as pp
from typing import Dict, Optional, Union
import re
import sys
sys.path.append('/Users/ivan/Documents/GitHub/PDP-11')


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
        - 'binary': бинарное представление команды
        """
        compiled = []
        current_address = 0o1000  # Начальный адрес (восьмеричный)

        for line in source_lines:
            line = line.strip()
            if not line:  # Пропускаем пустые строки
                continue

            # Игнорируем директиву . = 1000
            if line.startswith(". = "):
                continue

            # Разбираем строку
            parsed = self.parse(line)
            if "error" in parsed:
                continue

            # Генерируем бинарное представление команды
            binary = self.generate_binary(parsed)


            entry = {
                'adr': f"{current_address:06o}",  # Адрес в 6-значном восьмеричном формате
                'label': parsed.get('label', [''])[0] if 'label' in parsed else '',
                'cmd': line.split(';')[0].strip(),  # Вся команда до комментария
                'comment': parsed.get('comment', ''),
                'binary': binary
            }

            compiled.append(entry)

            # Определяем длину команды в байтах
            cmd_length = len(binary)  # Размер команды в байтах
            current_address += cmd_length

        return compiled

    def generate_binary(self, parsed: dict) -> list[str]:
        """
        Генерирует бинарное представление команды в точном соответствии с примером
        """
        cmd = parsed['command'].lower()
        args = parsed.get('args', [])
        binary = []

        if cmd == 'mov':
            # MOV src, dst: 01SSDD
            src = self.parse_arg(args[0])
            dst = self.parse_arg(args[1])

            # Формируем код команды
            opcode = 0o01  # MOV

            # Обработка режима адресации источника
            if src['mode'] == 27:  # Непосредственная адресация #
                src_code = 0o27  # Режим 27 (непосредственная адресация)
            else:
                src_code = (src['mode'] << 3) | src['regnum']

            dst_code = (dst['mode'] << 3) | dst['regnum']

            # Первое слово команды (little-endian)
            cmd_word = (opcode << 12) | (src_code << 6) | dst_code
            binary.append(f"{cmd_word & 0xff:02x}")  # Младший байт
            binary.append(f"{(cmd_word >> 8) & 0xff:02x}")  # Старший байт

            # Если есть непосредственное значение
            if src['additional_value'] is not None:
                val = src['additional_value']
                binary.append(f"{val & 0xff:02x}")  # Младший байт значения
                binary.append(f"{(val >> 8) & 0xff:02x}")  # Старший байт значения

        elif cmd == 'add':
            # ADD src, dst: 06SSDD
            src = self.parse_arg(args[0])
            dst = self.parse_arg(args[1])

            opcode = 0o06  # ADD
            src_code = (src['mode'] << 3) | src['regnum']
            dst_code = (dst['mode'] << 3) | dst['regnum']

            cmd_word = (opcode << 12) | (src_code << 6) | dst_code
            binary.append(f"{cmd_word & 0xff:02x}")  # Младший байт
            binary.append(f"{(cmd_word >> 8) & 0xff:02x}")  # Старший байт

        elif cmd == 'halt':
            # HALT: 000000
            binary.append("00")
            binary.append("00")

        return binary

    def generate_hex_file(self, compiled: list[dict], filename: str):
        """
        Генерирует hex-файл из скомпилированных данных
        """
        with open(filename, 'w') as f:
            # Заголовок (адрес и длина)
            total_bytes = sum(len(item['binary']) for item in compiled)
            f.write(f"0200 {total_bytes:04x}\n")

            # Данные (по одному байту на строку)
            for item in compiled:
                for byte in item['binary']:
                    f.write(f"{byte}\n")


source = [
    ". = 1000",
    "mov #2, R0",
    "mov #3, R1",
    "add R0, R1",
    "halt"
]

parser = PDP11Parser()
compiled = parser.compile(source)
print(compiled)
parser.generate_hex_file(compiled, "output.hex")