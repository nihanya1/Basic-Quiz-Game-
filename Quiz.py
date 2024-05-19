import tkinter as tk
from tkinter import messagebox

# Quiz data
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"}
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Game")
        
        self.score = 0
        self.question_index = 0
        
        self.question_label = tk.Label(root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 14), width=20, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.option_buttons.append(btn)
        
        self.next_button = tk.Button(root, text="Next", font=("Arial", 14), command=self.next_question)
        self.next_button.pack(pady=20)
        
        self.load_question()
    
    def load_question(self):
        question_data = questions[self.question_index]
        self.question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option)
    
    def check_answer(self, idx):
        selected_option = self.option_buttons[idx].cget("text")
        correct_answer = questions[self.question_index]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Your answer is incorrect!\nCorrect answer: {correct_answer}")
    
    def next_question(self):
        self.question_index += 1
        if self.question_index < len(questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Your final score is {self.score} out of {len(questions)}.")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
