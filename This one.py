import tkinter as tk
from tkinter import messagebox


class QuizApp:
    def __init__(self, root):
        # Initialize the quiz application yes
        self.root = root
        self.root.title("Quiz App")

        # Define a list of questions, each represented as a dictionary
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Paris", "Berlin", "Madrid"],
                "answer": "Paris"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "answer": "4"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Saturn", "Jupiter"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the capital of New Zealand?",
                "options": ["Auckland", "Wellington", "Christchurch", "Dunedin"],
                "answer": "Wellington"
            },
        ]

        # Initialize variables to keep track of the current question and score
        self.current_question = 0
        self.score = 0
        self.total_questions = len(self.questions)

        # Initialize the question label
        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)

        # Initialize radio buttons and their variables for answer choices
        self.option_vars = []
        self.option_buttons = []
        for i in range(4):
            var = tk.StringVar()
            var.set("")
            self.option_vars.append(var)
            option_button = tk.Radiobutton(
                root, text="", variable=var, value="", font=("Arial", 12))
            option_button.pack()
            self.option_buttons.append(option_button)

        # Initialize the "Next" button
        self.next_button = tk.Button(root, text="Next", command=self.check_answer)
        self.next_button.pack()

        # Initialize the score label
        self.score_label = tk.Label(root, text="", font=("Arial", 14))
        self.score_label.pack(pady=20)

        # Initialize the "Retry" button (initially hidden)
        self.retry_button = tk.Button(root, text="Retry", command=self.retry_quiz, state=tk.DISABLED)
        self.retry_button.pack_forget()  # Hide retry button initially

        # Start the quiz by displaying the first question
        self.update_question()

    def update_question(self):
        # Display the current question and answer options
        if self.current_question < self.total_questions:
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            options = question_data["options"]
            for i in range(4):
                self.option_buttons[i].config(
                    text=options[i], variable=self.option_vars[self.current_question], value=options[i])
        else:
            self.hide_question()  # Hide the question and options
            self.show_score()  # Show the score

    def check_answer(self):
        # Check the selected answer and update the score
        selected_option = self.option_vars[self.current_question].get()
        correct_answer = self.questions[self.current_question]["answer"]

        if not selected_option:
            messagebox.showerror("Error", "Please select an answer.")
            return

        if selected_option == correct_answer:
            self.score += 1

        self.current_question += 1

        for var in self.option_vars:
            var.set("")

        if self.current_question < self.total_questions:
            self.update_question()
        else:
            self.hide_question()  # Hide the question and options
            self.show_score()  # Show the score

    def hide_question(self):
        # Hide the question label, radio buttons, and next button
        self.question_label.pack_forget()
        for button in self.option_buttons:
            button.pack_forget()
        self.next_button.pack_forget()

    def show_score(self):
        # Show the score and the retry button
        score_text = f"You got {self.score}/{self.total_questions} questions correct"
        self.score_label.config(text=score_text)
        self.retry_button.pack()  # Show retry button
        self.retry_button.config(state=tk.NORMAL)  # Enable retry button

    def retry_quiz(self):
        # Reset the quiz and hide the retry button
        self.current_question = 0
        self.score = 0
        self.score_label.config(text="")
        self.retry_button.pack_forget()  # Hide retry button when retrying
        self.update_question()  # Show the first question and options again
        self.question_label.pack()
        for button in self.option_buttons:
            button.pack()
        self.next_button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.geometry('400x330')
    root.title("Quiz")
    root.resizable(False, False)
    root.mainloop()
