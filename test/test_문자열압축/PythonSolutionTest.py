import unittest
from 문자열압축 import PythonSolution as source


class MyTestCase(unittest.TestCase):
    def test_default_case(self):
        test_case = {"aabbaccc": 7,
                     "ababcdcdababcdcd": 9,
                     "abcabcdede": 8,
                     "abcabcabcabcdededededede": 14,
                     "xababcdcdababcdcd": 17}
        for test_input, test_pass in test_case.items():
            with self.subTest(test_input):
                self.assertEqual(source.solution(test_input), test_pass)


if __name__ == '__main__':
    unittest.main()
