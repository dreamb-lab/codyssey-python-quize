import unittest
from quiz import Quiz


class TestQuiz(unittest.TestCase):

    def setUp(self):
        self.quiz = Quiz(
            "파이썬 파일의 확장자는?",
            [".py", ".exe", ".txt", ".html"],
            1
        )

    def test_correct_answer(self):
        self.assertTrue(self.quiz.check_answer(1))

    def test_wrong_answer(self):
        self.assertFalse(self.quiz.check_answer(2))

    def test_to_dict(self):
        expected = {
            "question": "파이썬 파일의 확장자는?",
            "choices": [".py", ".exe", ".txt", ".html"],
            "answer": 1
        }
        self.assertEqual(self.quiz.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
