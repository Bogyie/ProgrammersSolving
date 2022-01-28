import unittest
from 타겟넘버 import PythonSolution as source


class MyTestCase(unittest.TestCase):
    def test_default_case(self):
        test_cases = [
            ({'numbers': [1, 1, 1, 1, 1], 'target':3}, 5),
            ({'numbers': [4, 1, 2, 1], 'target':4}, 2)
        ]

        for test_case, result in test_cases:
            with self.subTest(numbers=test_case['numbers'], target=test_case['target']):
                self.assertEqual(source.solution(**test_case), result)


if __name__ == '__main__':
    unittest.main()