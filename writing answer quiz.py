import tkinter as tk
from tkinter import messagebox


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        ]
        self.current_question = 0
        self.score = 0
        self.total_questions = len(self.questions)

        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Arial", 12))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.score_label = tk.Label(root, text="", font=("Arial", 14))
        self.score_label.pack(pady=20)

        self.retry_button = tk.Button(root, text="Retry", command=self.retry_quiz, state=tk.DISABLED)
        self.retry_button.pack()

        self.update_question()

    def update_question(self):
        if self.current_question < self.total_questions:
            self.question_label.config(text=self.questions[self.current_question]["question"])
        else:
            self.show_score()

    def check_answer(self):
        user_answer = self.answer_entry.get()
        correct_answer = self.questions[self.current_question]["answer"]

        if user_answer.lower() == correct_answer.lower():
            self.score += 1

        self.current_question += 1
        self.answer_entry.delete(0, tk.END)

        if self.current_question < self.total_questions:
            self.update_question()
        else:
            self.show_score()

    def show_score(self):
        score_text = f"Your Score: {self.score}/{self.total_questions}"
        self.score_label.config(text=score_text)
        self.retry_button.config(state=tk.NORMAL)

    def retry_quiz(self):
        self.current_question = 0
        self.score = 0
        self.score_label.config(text="")
        self.retry_button.config(state=tk.DISABLED)
        self.update_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
