# game.py
import json
import os
from quiz import Quiz

class QuizGame:
    def __init__(self, filename="state.json"):
        self.filename = filename
        self.quizzes = []
        self.best_score = 0
        self.load_data()

    def load_data(self):
        """state.json 파일에서 퀴즈와 최고 점수를 불러옴"""
        if not os.path.exists(self.filename):
            print("📂 저장된 데이터 파일이 없습니다. 기본 퀴즈 데이터로 시작합니다.")
            self.load_default_quizzes()
            self.save_data()
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                loaded_quizzes = data.get("quizzes", [])
                self.best_score = data.get("best_score", 0)
                
                self.quizzes = [
                    Quiz(q["question"], q["choices"], q["answer"]) 
                    for q in loaded_quizzes
                ]
                print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고 점수: {self.best_score}점)")
        except Exception:
            print("⚠️ 데이터 파일에 문제가 있어 기본 데이터로 복구합니다.")
            self.load_default_quizzes()
            self.save_data()

    def save_data(self):
        """현재 데이터를 state.json에 저장"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score
        }
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_default_quizzes(self):
        """기본 퀴즈 5개 세팅"""
        default_data = [
            ("Python의 창시자는 누구인가요?", ["귀도 반 로섬", "리누스 토르발스", "제임스 고슬링", "데니스 리치"], 1),
            ("다음 중 파이썬의 기본 데이터 타입이 아닌 것은?", ["int", "str", "array", "dict"], 3),
            ("파이썬에서 함수를 정의할 때 사용하는 키워드는?", ["func", "define", "def", "function"], 3),
            ("다음 중 참(True)과 거짓(False)을 나타내는 데이터 타입은?", ["bool", "float", "char", "tuple"], 1),
            ("깃(Git)에서 원격 저장소의 내용을 가져와 로컬에 합치는 명령어는?", ["git push", "git pull", "git commit", "git init"], 2)
        ]
        self.quizzes = [Quiz(q, c, a) for q, c, a in default_data]
        self.best_score = 0

    def get_validated_input(self, prompt, min_val, max_val):
        """숫자 입력 예외 처리 (잘못 입력해도 프로그램이 안 뻗게 방지)"""
        while True:
            try:
                user_input = input(prompt).strip()
                value = int(user_input)
                if min_val <= value <= max_val:
                    return value
                print(f"⚠️ {min_val}~{max_val} 사이의 숫자를 입력해주세요.")
            except ValueError:
                print("⚠️ 숫자만 입력해주세요.")

    def play_quiz(self):
        """퀴즈 풀기 기능"""
        if not self.quizzes:
            print("❌ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📝 퀴즈 시작! (총 {len(self.quizzes)}문제)")
        score = 0

        for idx, quiz in enumerate(self.quizzes, 1):
            quiz.display(idx)
            user_ans = self.get_validated_input("정답 입력 (1-4): ", 1, 4)
            
            if quiz.check_answer(user_ans):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 틀렸습니다! 정답은 {quiz.answer}번 입니다.")

        print(f"\n🏆 결과: 총 {score}점")
        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수 달성!")
            self.save_data()

    def add_quiz(self):
        """퀴즈 추가 기능"""
        print("\n📌 새로운 퀴즈 추가")
        question = input("문제 입력: ").strip()
        choices = [input(f"선택지 {i}: ").strip() for i in range(1, 5)]
        answer = self.get_validated_input("정답 번호 (1-4): ", 1, 4)
        
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_data()
        print("✅ 퀴즈가 추가되었습니다!")

    def show_quizzes(self):
        """퀴즈 목록 보기"""
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for idx, q in enumerate(self.quizzes, 1):
            print(f"[{idx}] {q.question}")

    def show_score(self):
        """점수 확인"""
        print(f"\n🏆 현재 최고 점수: {self.best_score}점")

    def run(self):
        """메인 메뉴 실행"""
        while True:
            print("\n====================")
            print("  🎯 나만의 퀴즈 게임")
            print("====================")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            print("====================")
            
            choice = self.get_validated_input("선택: ", 1, 5)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quizzes()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                print("👋 프로그램을 종료합니다.")
                break