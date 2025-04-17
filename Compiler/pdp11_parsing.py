import pyparsing as pp


class Data:
    """
    Здесь мы определяем допустимые команды и регистры.
    """
    commands = {"mov", "add", "sub", "halt", "inc"}  # Набор допустимых команд
    registers = {f"R{x}" for x in range(8)} | {"SP", "PC"} # Набор допустимых имен регистров (R0 - R7)
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
        identifier = pp.Word(pp.alphas + "_", pp.alphanums + "_") # Идентификатор (метка, переменная)
        number = pp.Combine(
            pp.Optional(pp.oneOf("+ -")) + pp.Word(pp.nums) # Обрабатывает числа со знаком
        ).addParseAction(lambda t: int(t[0])) # Преобразует разобранное число в целое число

        reg = (
            pp.Combine(pp.CaselessLiteral("R") + pp.Word(pp.nums)) | # Соответствует именам регистров (например, R0, R1)
            pp.CaselessLiteral("SP") |
            pp.CaselessLiteral("PC")
        ).setParseAction(lambda t: t[0].upper())

        # Способы адресации
        immediate = pp.Combine("#" + (number | identifier)) # Непосредственное значение (например, #10, #метка)
        absolute = pp.Combine("@" + pp.Optional("#") + (number | identifier)) # Абсолютный адрес (например, @1000, @#variable)
        reg_deferred = pp.Combine("(" + reg + ")") | pp.Combine("@" + reg) # Регистровая адресация (например, (R0), @R1)

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
        ).setParseAction(lambda t: t[0].replace(" ", "")) # Автоинкремент (например, (R0)+)

        auto_dec = pp.Combine(
            "-" + "(" + reg + ")"
        ).setParseAction(lambda t: t[0].replace(" ", "")) # Автодекремент (например, -(R1))

        auto_dec_indirect = pp.Combine(
            "@-" + "(" + reg + ")"
        ).setParseAction(lambda t: t[0].replace(" ", "")) # Косвенный автодекремент  @-(R1)

        indexed = pp.Combine(
            pp.Optional(number, default="0") +
            "(" + reg + ")" +
            pp.Optional("+", default="")
        ) #индексированная адресация

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

        label = (identifier + pp.Suppress(":")).setResultsName("label", listAllMatches=True)  # Метка (идентификатор, за которым следует двоеточие)
        command = pp.oneOf(list(Data.commands), caseless=True).setResultsName("command") # Команда (из списка допустимых команд)
        args = pp.Group(
            parameter + pp.Suppress(",") + parameter
        ).setResultsName("args") | pp.Group(parameter).setResultsName("args") # Аргументы команды
        comment = pp.Suppress(";") + pp.restOfLine.setResultsName("comment") # Комментарий (начинается с ";")

        self.parser = pp.ZeroOrMore(label) + command + pp.Optional(args) + pp.Optional(comment)

    def parse(self, line):
        try:
            result = self.parser.parseString(line, parseAll=True).asDict()  # Разбирает строку и преобразует результаты в словарь
            self.post_process(result) # Выполняет постобработку результатов
            self.validate(result) # Выполняет валидацию результатов
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

        if 'args' in result: # Если в результате есть аргументы
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

        cmd = result['command'].lower() # Получаем команду в нижнем регистре
        if cmd in {'mov', 'add', 'sub'} and len(result.get('args', [])) != 2:
            raise ValueError(f"Команда {cmd} требует 2 аргумента")
        elif cmd == 'inc' and len(result.get('args', [])) != 1:
            raise ValueError("Команда inc требует 1 аргумента")
