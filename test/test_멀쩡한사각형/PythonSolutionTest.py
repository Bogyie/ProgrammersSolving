import unittest
from 멀쩡한사각형 import PythonSolution as source


class MyTestCase(unittest.TestCase):
    def test_default_case(self):
        test_cases = [
            ({'w': 8, 'h': 12}, 80)
        ]

        for test_case, result in test_cases:
            with self.subTest(w=test_case['h'], h=test_case['h']):
                self.assertEqual(source.solution(**test_case), result)


if __name__ == '__main__':
    unittest.main()