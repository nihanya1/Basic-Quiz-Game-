class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question, options):
        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect. The correct answer is:", correct_answer)

    def start_quiz(self):
        for question, options, correct_answer in self.questions:
            self.display_question(question, options)
            user_answer = input("Enter your answer (1, 2, 3, etc.): ")
            if not user_answer.isdigit() or int(user_answer) < 1 or int(user_answer) > len(options):
                print("Invalid input. Please enter a valid option.")
                continue
            self.check_answer(options[int(user_answer) - 1], correct_answer)
        print("Quiz completed!")
        print("Your final score is:", self.score)


if __name__ == "__main__":
    questions = [
        ("What is the capital of France?", ["Paris", "London", "Berlin"], "Paris"),
        ("What is 2 + 2?", ["3", "4", "5"], "4"),
        ("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter"], "Mars")
    ]

    quiz = Quiz(questions)
    quiz.start_quiz()
