import unittest
from SourceTemplate.SolutionTemplate import PythonSolution as source


class MyTestCase(unittest.TestCase):
    def test_default_case(self):
        test_case = {"aabbaccc": 7,
                     "ababcdcdababcdcd": 9}
        for test_input, test_pass in test_case.items():
            with self.subTest(test_input):
                self.assertEqual(source.solution(test_input), test_pass)


if __name__ == '__main__':
    unittest.main()