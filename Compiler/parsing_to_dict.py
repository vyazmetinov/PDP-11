import pyparsing as pp


class Data:
    labels = frozenset({"loop"})
    command = frozenset({"mov", "add", "sub", "halt", "inc"})
    different_parameters = frozenset(
        {f'(R{x})' for x in range(8)} |
        {f'(R{x})+' for x in range(8)} |
        {f'@R{x}' for x in range(8)} |
        {f'@(R{x})+' for x in range(8)} |
        {f'@R{x}' for x in range(8)} |
        {f'-(R{x})' for x in range(8)} |
        {f'@-(R{x})' for x in range(8)} |
        {f'2R{x}' for x in range(8)} |
        {f'2(R{x})' for x in range(8)} |
        {f'@2(R{x})' for x in range(8)} |
        {str(x) for x in range(65536)} |
        {f'@{x}' for x in range(65536)}
    )
    parameters = frozenset(
        {"R0", "R1", "R2", "R3", "R4", "R5",
         "R6", "R7"} | different_parameters
    )
    values = frozenset(
        {f'#{x}' for x in range(11)} |
        {f'@#{x}'for x in range(-128, 128)} |
        {str(x) for x in range(65536)}
    )

    @classmethod
    def is_valid_value(cls, val):
        return val in cls.values

    @classmethod
    def is_valid_label(cls, lbs):
        return lbs in cls.labels

    @classmethod
    def is_valid_command(cls, cmd):
        return cmd in cls.command

    @classmethod
    def is_valid_parameter(cls, prm):
        return str(prm) in cls.parameters


class BlocksOfRule:
    @classmethod
    def init_blocks(cls):
        cls.label = pp.Word(pp.alphas) + pp.Suppress(":")
        cls.command_name = pp.Word(pp.alphas).setResultsName("command")

        r_num = pp.Word(pp.nums)
        r_prefix = pp.Optional(pp.Literal("@") + pp.Optional(pp.White()))
        r_suffix = pp.Optional(pp.Literal("+"))
        r_body = pp.CaselessLiteral("R") + r_num
        cls.numeric_address = pp.Word(pp.nums).setParseAction(lambda t: int(t[0]))
        cls.absolute_address = pp.Combine(
            pp.Literal("@") + pp.Word(pp.nums)
        ).setParseAction(lambda t: t[0])

        cls.register = pp.Combine(
            r_prefix +
            pp.Optional(r_num + pp.Optional(pp.White())) +
            pp.Optional(pp.Literal("-") + pp.Optional(pp.White())) +
            pp.Optional(pp.Literal("@") + pp.Optional(pp.White())) +
            pp.Optional(pp.Literal("(") + pp.Optional(pp.White())) +
            r_body +
            pp.Optional(pp.Literal(")") + pp.Optional(pp.White())) +
            r_suffix
        ).setParseAction(lambda t: ''.join(t[0].split()))

        cls.immediate_val = pp.Combine(
            pp.Optional(pp.Literal("@") + pp.Optional(pp.White())) +
            pp.Literal("#") +
            r_num
        ).setParseAction(lambda t: ''.join(t[0].split()))

        cls.register_first_command = (cls.register |
                                      cls.immediate_val |
                                      cls.numeric_address |
                                      cls.absolute_address
                                      )
        cls.register_second_command = (cls.register |
                                       cls.immediate_val |
                                       cls.numeric_address |
                                       cls.absolute_address
                                       )

        cls.literal_comma = pp.Suppress(",")
        cls.comment = (
                pp.Suppress(";") +
                pp.Optional(pp.White()).suppress() +
                pp.restOfLine().setResultsName("comment")
                .setParseAction(lambda tokens: str(tokens[0]).strip())
        )


BlocksOfRule.init_blocks()


def parse_line():
    rule = (
        pp.Optional(BlocksOfRule.label.setResultsName("label")) +
        BlocksOfRule.command_name +

        pp.Optional(
            BlocksOfRule.register_first_command +
            pp.Optional(BlocksOfRule.literal_comma +
                        BlocksOfRule.register_second_command)
        ).setResultsName("arguments") +

        pp.Optional(BlocksOfRule.comment.setResultsName("comment"))
    )
    return rule


def check(result_dict):
    for k in result_dict.keys():
        if k == "label":
            if not Data.is_valid_label(result_dict[k]):
                raise ValueError(f"Unknown label: {result_dict[k]}")
        if k == "command_name":
            if not Data.is_valid_command(result_dict[k]):
                raise ValueError(f"Unknown command name: {result_dict[k]}")
        if k == "parameters":
            for param in result_dict[k]:
                if not Data.is_valid_parameter(param) and not Data.is_valid_value(param):
                    raise ValueError(f"Unknown parameter: {param}")
                if (result_dict["command_name"] == "add") and \
                        sum([result_dict[k].count(x) for x in Data.values]) == 2:
                    raise ValueError("the source and destination cannot both be #")


def check_none(dictionary):
    return {k: v for k, v in dictionary.items() if
            v is not None and
            not (isinstance(v, str) and v == 'None') and
            not (isinstance(v, list) and not v)
            }


def parse_to_dict(line):
    parser = parse_line()
    result = parser.parseString(line, parseAll=True)

    arguments = result.get("arguments", [])
    parameters = []

    if len(arguments) > 0:
        parameters.append(arguments[0])
    if len(arguments) > 1:
        parameters.append(arguments[1])

    temp_dict = {
        "label": result.get("label", [None])[0],
        "command_name": result.command,

        "parameters": parameters,
        "comment": str(*result.get("comment", [None]))
    }

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
