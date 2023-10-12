# Import the tkinter library to create a GUI application.
import tkinter as tk
# Import messagebox and filedialog modules from tkinter for displaying messages and opening file dialogs.
from tkinter import messagebox, filedialog


# Create a class for the QuizApp.
class QuizApp:
    def __init__(self, root):
        # Initialize the root window for the application.
        self.root = root
        self.root.title("Quiz")

        # Define a list of quiz categories.
        self.categories = ["Flags", "Programming", "General Knowledge"]
        self.selected_category = None

        # Create a label widget for selecting a quiz category.
        self.category_label = tk.Label(root, text="Select a category:", font=("Arial", 14))
        self.category_buttons = []

        # Create a frame for displaying quiz questions.
        self.question_frame = tk.Frame(root)

        # Define a dictionary of quiz questions and answers.
        self.questions = {
            "Flags": [
                {
                    "question": "Which flag is this?🌈",
                    "options": ["3", "4", "1", "2"],
                    "answer": "3"
                },
                {
                    "question": "Which flag is this?",
                    "options": ["2", "3", "4", "5"],
                    "answer": "2"
                },
            ],
            "Programming": [
                {
                    "question": "Which Of The Following?",
                    "options": ["1", "3", "4", "2"],
                    "answer": "1"
                },
                {
                    "question": "Which Of The Following?",
                    "options": ["2", "3", "4", "1"],
                    "answer": "2"
                },
            ],
            "General Knowledge": [
                {
                    "question": "What is the most common surname\r"
                                " in the United States?",
                    "options": ["Brown", "Smith", "Johnson", "Williams"],
                    "answer": "Smith"
                },
                {
                    "question": "What country drinks the most\r"
                                " coffee per capita?",
                    "options": ["Finland", "Norway", "Iceland", "Denmark"],
                    "answer": "Finland"
                },
            ],
        }

        # Initialize quiz variables.
        self.current_question = 0
        self.score = 0
        self.total_questions = 0

        # Create a label for displaying the quiz question.
        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 14))

        # Create variables and buttons for quiz options.
        self.option_vars = []
        self.option_buttons = []

        # Create a button for moving to the next question.
        self.next_button = tk.Button(self.question_frame, text="Next", command=self.check_answer)

        # Create a label for displaying the quiz score.
        self.score_label = tk.Label(self.question_frame, text="", font=("Arial", 14))

        # Create a button for starting the quiz again.
        self.retry_button = tk.Button(self.question_frame, text="Start again", command=self.retry_quiz)

        # Initialize the quiz logic.
        self.question_logic()

        # Create a button for saving quiz results.
        self.save_button = tk.Button(self.question_frame, text="Save results", command=self.save_to_file)
        self.save_button.pack()

    def question_logic(self):
        # Display the category selection label and buttons.
        self.category_label.pack(pady=20)
        for category in self.categories:
            # Create buttons for each category and associate a callback function to select a category.
            button = tk.Button(root, text=category, command=lambda c=category: self.select_category(c))
            button.pack()
            self.category_buttons.append(button)

        # Create a frame for quiz questions and answers.
        self.question_frame = tk.Frame(root)

        # Create a label for displaying quiz questions.
        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)

        # Create option buttons for quiz answers.
        self.option_buttons = []
        for i in range(4):
            var = tk.StringVar()
            var.set("")
            self.option_vars.append(var)

        for i in range(4):
            option_button = tk.Radiobutton(
                self.question_frame, text="", value="", font=("Arial", 12))
            option_button.pack()
            self.option_buttons.append(option_button)

        # Create a button to move to the next question.
        self.next_button = tk.Button(self.question_frame, text="Next", command=self.check_answer)
        self.next_button.pack()

        # Create a label for displaying the quiz score.
        self.score_label = tk.Label(self.question_frame, text="", font=("Arial", 14))
        self.score_label.pack(pady=20)

        # Create a button to start the quiz again.
        self.retry_button = tk.Button(self.question_frame, text="Start again", command=self.retry_quiz)
        self.retry_button.pack_forget()

        # Create a button for saving quiz results and hide it initially.
        self.save_button = tk.Button(self.question_frame, text="Save results", command=self.save_to_file)
        self.save_button.pack_forget()

        # Display the "Start again" button.
        self.retry_button.pack()

    def save_to_file(self):
        results = """
        Category: {}
        Total Questions: {}
        Correct Answers: {}

        Thank you for playing the quiz!
        """.format(self.selected_category, self.total_questions, self.score)

        # Ask the user to select a file for saving
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        # Check if the user canceled the file dialog
        if not file_path:
            return

        try:
            # Write the data to the selected file
            with open(file_path, 'w') as file:
                file.write(results)
            messagebox.showinfo("File Saved", "Data saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", "Error occurred while saving the file:\n{}".format(e))

    def select_category(self, category):
        # Set the selected category and reset quiz variables.
        self.selected_category = category
        self.total_questions = len(self.questions[category])
        self.current_question = 0
        self.score = 0

        # Hide the category selection elements and display the quiz question frame.
        self.category_label.pack_forget()
        for button in self.category_buttons:
            button.pack_forget()
        # Display the first quiz question.
        self.question_frame.pack()
        self.update_question()

    # Method to update the question and answer options.
    def update_question(self):
        if self.selected_category is not None:  # Check if category is selected
            if self.current_question < self.total_questions:
                # Display the current quiz question and options.
                question_data = self.questions[self.selected_category][self.current_question]
                self.question_label.config(text=question_data["question"])
                options = question_data["options"]
                num_options = len(options)
                for i in range(num_options):
                    self.option_buttons[i].config(
                        text=options[i], variable=self.option_vars[self.current_question], value=options[i])
                for j in range(num_options, 4):
                    self.option_buttons[j].pack_forget()
            else:
                # Hide the question frame and display the quiz score.
                self.hide_question()
                self.show_score()

    def check_answer(self):
        # Check if an option is selected and compare it to the correct answer.
        selected_option = self.option_vars[self.current_question].get()
        correct_answer = self.questions[self.selected_category][self.current_question]["answer"]

        if not selected_option:
            messagebox.showerror("Error", "Please select an answer.")
            return

        if selected_option == correct_answer:
            self.score += 1

        self.current_question += 1

        for var in self.option_vars:
            var.set("")

        if self.current_question < self.total_questions:
            # If there are more questions, move to the next question.
            self.update_question()
        else:
            # If all questions are answered, hide the question frame and show the score.
            self.hide_question()
            self.show_score()

    def hide_question(self):
        # Hide the question label, option buttons, and next button.
        self.question_label.pack_forget()
        for button in self.option_buttons:
            button.pack_forget()
        self.next_button.pack_forget()

    def show_score(self):
        # Display the quiz score and the "Start again" and "Save results" buttons.
        score_text = f"You got {self.score}/{self.total_questions} correct answers"
        self.score_label.config(text=score_text)
        self.retry_button.pack()
        self.retry_button.config(state=tk.NORMAL)
        self.save_button.pack()
        self.save_button.config(state=tk.NORMAL)

    def show_category_selection(self):
        # Reset the selected category and display the category selection elements.
        self.selected_category = None
        self.category_label.pack()
        for button in self.category_buttons:
            button.pack()
        self.question_frame.pack_forget()
        self.update_question()

    def retry_quiz(self):
        # Reset quiz variables and display the first question.
        self.current_question = 0
        self.score = 0
        self.score_label.config(text="")
        self.retry_button.pack_forget()
        self.question_frame.pack_forget()
        self.update_question()
        self.question_logic()


# Check if the script is the main program.
if __name__ == "__main__":
    # Create the root window.
    root = tk.Tk()
    # Create an instance of the QuizApp class.
    app = QuizApp(root)
    # Set the window size and title.
    root.geometry('400x260')
    root.title("Quiz")
    # Disable window resizing.
    root.resizable(False, False)
    # Start the GUI event loop.
    root.mainloop()
