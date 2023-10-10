import tkinter as tk
from tkinter import messagebox, filedialog

 # hi
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz")
        self.categories = ["Category 1", "Category 2", "Category 3"]
        self.selected_category = None
        self.category_label = tk.Label(root, text="Select a category:", font=("Arial", 14))
        self.category_buttons = []
        self.question_frame = tk.Frame(root)
        self.questions = {
            "Category 1": [
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
            ],
            "Category 2": [
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
            ],
            "Category 3": [
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
            ],
        }
        self.current_question = 0
        self.score = 0
        self.total_questions = 0

        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 14))

        self.option_vars = []
        self.option_buttons = []
        self.next_button = tk.Button(self.question_frame, text="Next", command=self.check_answer)
        self.score_label = tk.Label(self.question_frame, text="", font=("Arial", 14))
        self.retry_button = tk.Button(self.question_frame, text="Start again", command=self.retry_quiz)
        self.question_logic()
        self.save_button = tk.Button(self.question_frame, text="Save Results", command=self.save_to_file)
        self.save_button.pack()

    def question_logic(self):
        self.category_label.pack(pady=20)
        for category in self.categories:
            button = tk.Button(root, text=category, command=lambda c=category: self.select_category(c))
            button.pack()
            self.category_buttons.append(button)
        self.question_frame = tk.Frame(root)
        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)

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

        self.next_button = tk.Button(self.question_frame, text="Next", command=self.check_answer)
        self.next_button.pack()

        self.score_label = tk.Label(self.question_frame, text="", font=("Arial", 14))
        self.score_label.pack(pady=20)

        self.retry_button = tk.Button(self.question_frame, text="Start again", command=self.retry_quiz)
        self.retry_button.pack_forget()

    def save_to_file(self):
        # Get the content you want to save (replace this with your data)
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
        self.selected_category = category
        self.total_questions = len(self.questions[category])
        self.current_question = 0
        self.score = 0
        self.category_label.pack_forget()
        for button in self.category_buttons:
            button.pack_forget()
        self.question_frame.pack()
        self.update_question()

    def update_question(self):
        if self.selected_category is not None:  # Check if category is selected
            if self.current_question < self.total_questions:
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
                self.hide_question()
                self.show_score()

    def check_answer(self):
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
            self.update_question()
        else:
            self.hide_question()
            self.show_score()

    def hide_question(self):
        self.question_label.pack_forget()
        for button in self.option_buttons:
            button.pack_forget()
        self.next_button.pack_forget()

    def show_score(self):
        score_text = f"You got {self.score}/{self.total_questions} correct answers"
        self.score_label.config(text=score_text)
        self.retry_button.pack()
        self.retry_button.config(state=tk.NORMAL)

    def show_category_selection(self):
        self.selected_category = None
        self.category_label.pack()
        for button in self.category_buttons:
            button.pack()
        self.question_frame.pack_forget()
        self.update_question()

    def retry_quiz(self):
        self.current_question = 0
        self.score = 0
        self.score_label.config(text="")
        self.retry_button.pack_forget()
        self.question_frame.pack_forget()
        self.update_question()
        self.question_logic()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.geometry('400x260')
    root.title("Quiz")
    root.resizable(False, False)
    root.mainloop()
