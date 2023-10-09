# Import the tkinter library for GUI
import tkinter as tk
from tkinter import messagebox


# Create a class for the Quiz Application
class QuizApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Quiz")  # Set the window title

        # Questions, options to choose from and the answers
        self.questions = [
            {
                "question": "What is 1 + 1?",
                "options": ["2", "4", "5", "6"],
                "answer": "2"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "answer": "4"
            },
            {
                "question": "What is 3 + 3?",
                "options": ["3", "4", "5", "6"],
                "answer": "6"
            },
            {
                "question": "What is 4 + 4?",
                "options": ["3", "4", "5", "8"],
                "answer": "8"
            },
            {
                "question": "What is 5 + 5?",
                "options": ["2", "3", "1", "10"],
                "answer": "10"
            },
            {
                "question": "What is 6 + 6?",
                "options": ["2", "window", "1", "12"],
                "answer": "12"
            },
            {
                "question": "What is 7 + 7?",
                "options": ["2", "window", "1", "14"],
                "answer": "14"
            },
            {
                "question": "What is 8 + 8?",
                "options": ["2", "window", "1", "16"],
                "answer": "16"
            },
            {
                "question": "What is 9 + 9?",
                "options": ["2", "window", "1", "18"],
                "answer": "18"
            },
            {
                "question": "What is 10 + 10?",
                "options": ["2", "window", "1", "20"],
                "answer": "20"
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
        self.option_vars = []  # List to store answer choice variables
        self.option_buttons = []  # List to store radio buttons
        for i in range(10):
            var = tk.StringVar()
            var.set("")  # Initialize the variable
            self.option_vars.append(var)

        for i in range(4):
            option_button = tk.Radiobutton(
                root, text="", value="", font=("Arial", 12))
            option_button.pack()
            self.option_buttons.append(option_button)

        # Initialize the "Next" button
        self.next_button = tk.Button(root, text="Next", command=self.check_answer)
        self.next_button.pack()

        # Initialize the score label
        self.score_label = tk.Label(root, text="", font=("Arial", 14))
        self.score_label.pack(pady=20)

        # Initialize the "Retry" button (initially hidden)
        self.retry_button = tk.Button(root, text="Start again", command=self.retry_quiz)
        self.retry_button.pack_forget()  # Hide retry button initially

        # Start the quiz by displaying the first question
        self.update_question()

    def update_question(self):
        # Display the current question and answer options
        if self.current_question < self.total_questions:
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            options = question_data["options"]

            # Create radio buttons dynamically based on the number of answer choices
            num_options = len(options)
            for i in range(num_options):
                self.option_buttons[i].config(
                    text=options[i], variable=self.option_vars[self.current_question], value=options[i])

            # Hide any remaining radio buttons (if any)
            for j in range(num_options, 4):
                self.option_buttons[j].pack_forget()
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
            var.set("")  # Clear the radio button selection

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
        score_text = f"You got {self.score}/{self.total_questions} correct answers"
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
    root = tk.Tk()  # Create the main window
    app = QuizApp(root)  # Initialize the QuizApp class
    root.geometry('400x300')  # Set the window size
    root.title("Quiz")  # Set the window title
    root.resizable(False, False)  # Disable window resizing
    root.mainloop()  # Start the main event loop
