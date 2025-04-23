import pyparsing as pp
import numpy as np

def cyrillic() -> str:
    return ''.join(np.vectorize(chr)(np.arange(0x0410, 0x0450)))

def parsing_mod() -> pp.ParserElement:
    command_name = pp.Word(pp.alphas)

    register = pp.Combine(pp.Word(pp.alphas, exact=1) + pp.Word(pp.nums, exact=1))

    immediate_value = pp.Suppress('#') + pp.Word(pp.nums)
    indirect_register = pp.Suppress('(') + register + pp.Suppress(')')
    indirect_register_inc = pp.Suppress('(') + register + pp.Suppress(')+')
    indirect_register_dec = pp.Suppress('-(') + register + pp.Suppress(')')
    indirect_address = pp.Suppress('@') + register
    indirect_address_dec = pp.Suppress('@-(') + register + pp.Suppress(')')

    argument = (
        immediate_value
        | register
        | indirect_register
        | indirect_register_inc
        | indirect_register_dec
        | indirect_address
        | indirect_address_dec
    )

    arguments = pp.Group(pp.Optional(argument) + pp.ZeroOrMore(pp.Suppress(',') + argument))

    label = pp.Word(pp.alphas) + pp.Optional(pp.Suppress(' ')) + pp.Suppress(":")

    comment = pp.Suppress(';') + pp.Optional(pp.Suppress(' ')) + pp.restOfLine()

    rule = pp.Optional(label) + command_name + pp.Optional(arguments) + pp.Optional(comment)

    return rule
