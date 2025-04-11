import unittest
from pdp11_parsing import PDP11Parser


class TestPDP11Parser(unittest.TestCase):
    def setUp(self):
        self.parser = PDP11Parser()

    def test_mov_immediate_to_register(self):
        test_cases = [
            ("mov #2, R0", {'command': 'mov', 'args': ['#2', 'R0']}),
            ("mov #3, R1", {'command': 'mov', 'args': ['#3', 'R1']}),
        ]

        for code, expected in test_cases:
            with self.subTest(code=code):
                result = self.parser.parse(code)
                self.assertEqual(result['command'].lower(), expected['command'])
                self.assertEqual(result['args'], expected['args'])

    def test_add_operations(self):
        test_cases = [
            ("add R0, R1", {'command': 'add', 'args': ['R0', 'R1']}),
            ("add #10, R3", {'command': 'add', 'args': ['#10', 'R3']}),
        ]

        for code, expected in test_cases:
            with self.subTest(code=code):
                result = self.parser.parse(code)
                self.assertEqual(result['command'].lower(), expected['command'])
                self.assertEqual(result['args'], expected['args'])

    def test_labels(self):
        test_cases = [
            ("loop: add #1, R0", {'label': ['loop'], 'command': 'add', 'args': ['#1', 'R0']}),
            ("loop  : add #1, R0", {'label': ['loop'], 'command': 'add', 'args': ['#1', 'R0']}),
        ]

        for code, expected in test_cases:
            with self.subTest(code=code):
                result = self.parser.parse(code)
                self.assertEqual(result['label'], expected['label'])
                self.assertEqual(result['command'].lower(), expected['command'])
                self.assertEqual(result['args'], expected['args'])

    def test_halt(self):
        test_cases = [
            ("halt", {'command': 'halt'}),
            ("halt ;    остановка процессора", {'command': 'halt', 'comment': '    остановка процессора'}),
        ]

        for code, expected in test_cases:
            with self.subTest(code=code):
                result = self.parser.parse(code)
                self.assertEqual(result['command'].lower(), expected['command'])
                if 'comment' in expected:
                    self.assertEqual(result['comment'], expected['comment'])

    def test_memory_addressing(self):
        test_cases = [
            ("mov (R0), R1", {'command': 'mov', 'args': ['(R0)', 'R1']}),
            ("mov (R0)+, R1", {'command': 'mov', 'args': ['(R0)+', 'R1']}),
            ("mov -(R0), R1", {'command': 'mov', 'args': ['-(R0)', 'R1']}),
            ("mov @R0, R1", {'command': 'mov', 'args': ['@R0', 'R1']}),
            ("mov @-(R0), R1", {'command': 'mov', 'args': ['@-(R0)', 'R1']}),
            ("inc @  (R3)+", {'command': 'inc', 'args': ['@(R3)+']}),
        ]

        for code, expected in test_cases:
            with self.subTest(code=code):
                result = self.parser.parse(code)
                self.assertEqual(result['command'].lower(), expected['command'])
                self.assertEqual(result['args'], expected['args'])

    def test_comments(self):
        test_cases = [
            ("mov #2, R0 ;R0 = 2", {'command': 'mov', 'args': ['#2', 'R0'], 'comment': 'R0 = 2'}),
            ("add R0, R1 ; R1 = R0 + R1", {'command': 'add', 'args': ['R0', 'R1'], 'comment': ' R1 = R0 + R1'}),
        ]

        for code, expected in test_cases:
            with self.subTest(code=code):
                result = self.parser.parse(code)
                self.assertEqual(result['command'].lower(), expected['command'])
                self.assertEqual(result['args'], expected['args'])
                self.assertEqual(result['comment'], expected['comment'])


if __name__ == '__main__':
    unittest.main(verbosity=2)