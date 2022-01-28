import unittest
from 오픈채팅방 import PythonSolution as source


class MyTestCase(unittest.TestCase):
    def test_default_case(self):
        test_cases = [
            ({'record': ["Enter uid1234 Muzi",
                         "Enter uid4567 Prodo",
                         "Leave uid1234",
                         "Enter uid1234 Prodo",
                         "Change uid4567 Ryan"]},
              ["Prodo님이 들어왔습니다.",
               "Ryan님이 들어왔습니다.",
               "Prodo님이 나갔습니다.",
               "Prodo님이 들어왔습니다."])
        ]

        for test_case, result in test_cases:
            with self.subTest(record=test_case['record']):
                self.assertEqual(source.solution(**test_case), result)


if __name__ == '__main__':
    unittest.main()