import unittest
from 멀쩡한사각형 import PythonSolution as source


class MyTestCase(unittest.TestCase):
    def test_default_case(self):
        test_cases = [
            ({'W': 8, 'H': 12}, 80)
        ]

        for test_case, result in test_cases:
            with self.subTest(numbers=test_case['numbers'], target=test_case['target']):
                self.assertEqual(source.solution(**test_case), result)


if __name__ == '__main__':
    unittest.main()