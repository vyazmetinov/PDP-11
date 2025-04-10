import pyparsing as pp


class Data:
    """
    Здесь мы определяем допустимые команды и регистры.
    """
    commands = {"mov", "add", "sub", "halt", "inc"}  # Набор допустимых команд
    registers = {f"R{x}" for x in range(8)}  # Набор допустимых имен регистров (R0 - R7)

    @classmethod
    def is_valid_register(cls, reg):
        """
        Проверяем, является ли данная строка допустимым именем регистра.
        """
        return reg.upper() in cls.registers


class PDP11Parser:
    def __init__(self):
        self.init_grammar()

    def init_grammar(self):
        # Базовые элементы
        identifier = pp.Word(pp.alphas + "_", pp.alphanums + "_")  # Идентификатор (метка, переменная)
        number = pp.Combine(
            pp.Optional(pp.oneOf("+ -")) + pp.Word(pp.nums)  # Обрабатывает числа со знаком
        ).addParseAction(lambda t: int(t[0]))  # Преобразует разобранное число в целое число

        reg = pp.Combine(
            pp.CaselessLiteral("R") + pp.Word(pp.nums)  # Соответствует именам регистров (например, R0, R1)
        )

        # Способы адресации
        immediate = pp.Combine("#" + (number | identifier))  # Непосредственное значение (например, #10, #метка)
        absolute = pp.Combine("@" + pp.Optional("#") + (number | identifier))  # Абсолютный адрес (например, @1000, @#variable)

        reg_deferred = pp.Combine("(" + reg + ")") | pp.Combine("@" + reg)  # Регистровая адресация (например, (R0), @R1)

        auto_inc_indirect = pp.Combine(
            "@" + pp.Optional(pp.White()) +
            "(" + pp.Optional(pp.White()) +
            reg +
            pp.Optional(pp.White()) + ")+"
        ).setParseAction(lambda t: '@(' + t[0][1:].replace(" ", "") + ')+') #  @(R0)+


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
        )   #индексированная адресация

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
        )   # параметр может быть чем угодно

        label = (identifier + pp.Suppress(":")).setResultsName("label")  # Метка (идентификатор, за которым следует двоеточие)

        command = pp.oneOf(list(Data.commands), caseless=True).setResultsName("command")  # Команда (из списка допустимых команд)

        args = pp.Group(
            parameter + pp.Suppress(",") + parameter
        ).setResultsName("args") | pp.Group(parameter).setResultsName("args") # Аргументы команды

        comment = pp.Suppress(";") + pp.restOfLine.setResultsName("comment")  # Комментарий (начинается с ";")

        self.parser = pp.Optional(label) + command + pp.Optional(args) + pp.Optional(comment)

    def parse(self, line):
        """
        Разбирает строку ассемблера и возвращает словарь с результатами разбора.
        """
        try:
            result = self.parser.parseString(line, parseAll=True).asDict()  # Разбирает строку и преобразует результаты в словарь
            self.post_process(result)  # Выполняет постобработку результатов
            self.validate(result)  # Выполняет валидацию результатов
            return result
        except pp.ParseException as e:
            return {"error": str(e)}  # Возвращает сообщение об ошибке при неудачном разборе

    def post_process(self, result):
        """
        Выполняет постобработку результатов разбора, например, нормализует регистры.
        """
        if 'args' in result:  # Если в результате есть аргументы
            args = []
            for arg in result['args']:
                if isinstance(arg, list):
                    processed = arg[0]
                else:
                    processed = ''.join(str(arg).split()) #Убираем пробелы

                if processed.upper().startswith('R'): # Приводим к верхнему регистру
                    processed = processed.upper()
                args.append(processed)
            result['args'] = args  # Обновляем аргументы в результате

    def validate(self, result):
        """
        Выполняет корректность результатов разбора
        """
        if 'args' in result:
            for arg in result['args']:
                if isinstance(arg, str) and arg.upper() in {'R8', 'R9'}:
                    raise ValueError("Недопустимый регистр (допустимы R0-R7)")
        cmd = result['command'].lower()  # Получаем команду в нижнем регистре
        if cmd in {'mov', 'add', 'sub'} and len(result.get('args', [])) != 2:
            raise ValueError(f"Команда {cmd} требует 2 аргумента")  # Проверяем количество аргументов для mov, add, sub
        elif cmd == 'inc' and len(result.get('args', [])) != 1:
            raise ValueError("Команда inc требует 1 аргумента")  # Проверяем количество аргументов для inc
            
    result_dict = check_none(temp_dict)

    check(result_dict)

    return result_dict


def parse_test():
    strs = [
        "mov #2, R0 ;R0 = 2",
        "mov #3, R1 ;R1 = 3",
        "add R0, R1 ; R1 = R0 + R1",
        "loop: add #1, R0",
        "loop  : add #1, R0",
        "halt ;    остановка процессора",
        "halt",
        "add #10, R3",
        "sub R1",
        "mov (R0), R1",
        "mov (R0)+, R1",
        "mov -(R0), R1",
        "mov @R0, R1",
        "mov @-(R0), R1",
        "inc @  (R3)+",
        "inc -(R3)",
        "inc 2(R3)",
        "inc @ 2(R3)",
        "mov @#100,R0",
        "mov 100, R0",
        "mov @100,R0",
        "add R0, R1"

    ]
    for i in strs:
        print(i, parse_to_dict(i))


if __name__ == "__main__":
    parse_test()
