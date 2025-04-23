import pytest
from pdp11_parsing import PDP11Parser

@pytest.mark.parametrize(
    "commands, expected",
    [
        ("mov #2, R0", {'command': 'mov','args': ['#2', 'R0']}),
        ("mov #3, R1", {'command': 'mov','args': ['#3', 'R1']}),
        ("mov (R0), R1", {'command': 'mov', 'args': ['(R0)', 'R1']}),
        ("mov (R0)+, R1", {'command': 'mov', 'args': ['(R0)+', 'R1']}),
        ("mov -(R0), R1", {'command': 'mov', 'args': ['-(R0)', 'R1']}),
        ("mov @R0, R1", {'command': 'mov', 'args': ['@R0', 'R1']}),
        ("mov @-(R0), R1", {'command': 'mov', 'args': ['@-(R0)', 'R1']}),
        ("mov #2, R0 ;R0 = 2", {'command': 'mov', 'args': ['#2', 'R0'], 'comment': 'R0 = 2'}),
        ("mov @#100, R0", {'command': 'mov', 'args': ['@#100', 'R0']}),
        ("mov 100, R0", {'command': 'mov', 'args': ['100', 'R0']}),
        ("mov @100, R0", {'command': 'mov', 'args': ['@100', 'R0']}),

        ("add R0, R1", {'command': 'add', 'args': ['R0', 'R1']}),
        ("add #10, R3", {'command': 'add', 'args': ['#10', 'R3']}),
        ("add R0, R1 ; R1 = R0 + R1", {'command': 'add', 'args': ['R0', 'R1'], 'comment': ' R1 = R0 + R1'}),

        ("loop: add #1, R0", {'label': ['loop'], 'command': 'add', 'args': ['#1', 'R0']}),
        ("loop  : add #1, R0", {'label': ['loop'], 'command': 'add', 'args': ['#1', 'R0']}),
        ("loop1:loop2: add #1, R0", {'label': ['loop1','loop2'], 'command': 'add', 'args': ['#1', 'R0']}),

        ("halt", {'command': 'halt'}),
        ("halt ;    остановка процессора", {'command': 'halt', 'comment': '    остановка процессора'}),

        ("inc @  (R3)+", {'command': 'inc', 'args': ['@(R3)+']}),
        ("INC @  (R3)+", {'command': 'inc', 'args': ['@(R3)+']}),

        ("mov -(PC), -(PC)", {'command': 'mov', 'args': ['-(PC)', '-(PC)']})
    ]
)

class TestPDP11Parser:
    def setup_method(self, method):
        self.parser = PDP11Parser()

    def test_mov_immediate_to_register(self,commands,expected):
        assert self.parser.parse(commands) == expected
if __name__ == '__main__':
    pytest.main([__file__])