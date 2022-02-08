import unittest
from 기능개발 import PythonSolution as source


class MyTestCase(unittest.TestCase):
    def test_default_case(self):
        test_cases = [
            ({'progresses': [93, 30, 55], 'speeds': [1, 30, 5]}, [2, 1]),
            ({'progresses': [95, 90, 99, 99, 80, 99], 'speeds': [1, 1, 1, 1, 1, 1]}, [1, 3, 2]),
        ]

        for test_case, result in test_cases:
            with self.subTest(progresses=test_case['progresses'], speeds=test_case['speeds']):
                self.assertEqual(source.solution(**test_case), result)


if __name__ == '__main__':
    unittest.main()
