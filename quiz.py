# quiz.py

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question      # 문제
        self.choices = choices        # 선택지 (4개 리스트)
        self.answer = answer          # 정답 번호 (1~4)

    def display(self, index):
        """퀴즈를 예쁘게 출력하는 기능"""
        print(f"\n----------------------------------------")
        print(f"[문제 {index}] {self.question}")
        print()
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")
        print(f"----------------------------------------")

    def check_answer(self, user_answer):
        """정답이 맞는지 확인하는 기능"""
        return user_answer == self.answer

    def to_dict(self):
        """파일 저장을 위해 딕셔너리로 변환"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }
