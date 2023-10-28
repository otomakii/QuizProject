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

        # Set the background color for the root window.
        self.root.configure(bg="#581b61")

        # Define a list of quiz categories.
        self.categories = ["Flags                         ", "Mythology               ", "General Knowledge"]
        self.selected_category = None

        # Create a label widget for selecting a quiz category.
        self.category_label = tk.Label(root, text="Select a category:", font=("Arial", 14),
                                       fg="yellow", bg="#581b61")
        self.category_buttons = []

        # Create a frame for displaying quiz questions.
        self.question_frame = tk.Frame(root, bg="#581b61")

        self.questions = {
            "Flags                         ": [
                {
                    "question": "What is the most common colour on world flags?",
                    "options": ["red", "white", "blue", "green"],
                    "answer": "red"
                },
                {
                    "question": "Which of these countries\r"
                                " has the most colours on their flag?",
                    "options": ["germany", "korea", "belgium", "france"],
                    "answer": "korea"
                },
                {
                    "question": "How many rings are in the olympic flag?",
                    "options": ["7", "4", "6", "5"],
                    "answer": "5"
                },
                {
                    "question": "What colours are on the flag of netherlands?",
                    "options": ["red, white, blue", "red, yellow, green", "green, blue", "yellow, white blue"],
                    "answer": "red, white, blue"
                },
                {
                    "question": "Which flag has a purple and green\r"
                                " feathered bird in the center?",
                    "options": ["ghana", "haiti", "Dominica", "bahamas"],
                    "answer": "Dominica"
                },
                {
                    "question": "What do you call the study of flags?",
                    "options": ["flagknowledge", "geography", "vexillology", "flagology"],
                    "answer": "vexillology"
                },
                {
                    "question": "Which flag is the only non-quadrilateral flag?",
                    "options": ["Sri lanka", "ecuador", "turkey", "Nepal"],
                    "answer": "Nepal"
                },
                {
                    "question": "How many stars are on the Chinese flag?",
                    "options": ["5", "4", "6", "1"],
                    "answer": "5"
                },
                {
                    "question": "How many stripes does the USA flag have?",
                    "options": ["50", "13", "51", "11"],
                    "answer": "13"
                },
                {
                    "question": "What is the colour order of Frances flag?",
                    "options": ["black, yellow, red", "red, blue, white", "green, white, red", "blue, white, red"],
                    "answer": "blue, white, red"
                },
            ],
            "Mythology               ": [
                {
                    "question": "Who is the god of the sky in Greek mythology?",
                    "options": ["zeus", "apollo", "aphrodite", "ares"],
                    "answer": "zeus"
                },
                {
                    "question": "Which planet is named after the\r"
                                " Roman God of war?",
                    "options": ["jupiter", "earth", "saturn", "mars"],
                    "answer": "mars"
                },
                {
                    "question": "Viking warriors go 2 after they die\r"
                                " according to Norse mythology?",
                    "options": ["heaven", "valhalla", "hell", "spirit realm"],
                    "answer": "valhalla"
                },
                {
                    "question": "Which Egyptian god has the head of a jackal?",
                    "options": ["anubis", "ra", "geb", "horus"],
                    "answer": "anubis"
                },
                {
                    "question": "Where do the gods live in Greek mythology?",
                    "options": ["atlantis", "asgard", "aztec", "mount olympus"],
                    "answer": "mount olympus"
                },
                {
                    "question": "Which Norse god carries a hammer?",
                    "options": ["loki", "odin", "thor", "captain america"],
                    "answer": "thor"
                },
                {
                    "question": "Which animal is associated\r"
                                " with Odin in Norse mythology?",
                    "options": ["albatross", "crow", "raven", "eagle"],
                    "answer": "raven"
                },
                {
                    "question": "What was the loch ness monster's nickname?",
                    "options": ["nessie", "nessy-wessy", "noch less", "scotlands monster"],
                    "answer": "nessie"
                },
                {
                    "question": "Who is the god associated with music, prophecy,\r"
                                " and the sun in Greek mythology?",
                    "options": ["hera", "apollo", "eros", "artemis"],
                    "answer": "apollo"
                },
                {
                    "question": "Who is the god of war?",
                    "options": ["chronos", "poseidon", "athena", "ares"],
                    "answer": "ares"
                },
            ],
            "General Knowledge": [
                {
                    "question": "Which is the smallest ocean?",
                    "options": ["Southern ocean", "Arctic ocean", "Indian ocean", "Atlantic ocean"],
                    "answer": "Arctic ocean"
                },
                {
                    "question": "On which time zone is London?",
                    "options": ["Central european standard time", "Eastern standard time",
                                "Australian eastern daylight Time", "Greenwich mean time"],
                    "answer": "Greenwich mean time"
                },
                {
                    "question": "What is the most common surname\r in the United States?",
                    "options": ["Smith", "Williams", "Johnson", "Brown"],
                    "answer": "Smith"
                },
                {
                    "question": "During which month is Thanksgiving celebrated?",
                    "options": ["January", "December", "November", "October"],
                    "answer": "November"
                },
                {
                    "question": "Lead Pipe, Wrench, Revolver, Dagger, Candlestick\r"
                                " are weapons in which board game?",
                    "options": ["Risk", "Monopoly", "Cluedo", "Mysterium"],
                    "answer": "Cluedo"
                },
                {
                    "question": "What country drinks the most coffee per capita?",
                    "options": ["Denmark", "Norway", "Iceland", "Finland"],
                    "answer": "Finland"
                },
                {
                    "question": "What is the longest river in the world?",
                    "options": ["Nile", "Amazon", "Congo", "Mississippi"],
                    "answer": "Nile"
                },
                {
                    "question": "What is Earths largest continent?",
                    "options": ["South america", "Asia", "North america", "Africa"],
                    "answer": "Asia"
                },
                {
                    "question": "Who painted the Mona Lisa?",
                    "options": ["Pablo Picasso", "Vincent van Gogh", "Michelangelo", "Leonardo da Vinci"],
                    "answer": "Leonardo da Vinci"
                },
                {
                    "question": "Which two planets in the solar system\r"
                                " have no moons?",
                    "options": ["Mercury and Venus", "Neptune and Jupiter", "Mars and Earth", "Saturn and Uranus"],
                    "answer": "Mercury and Venus"
                },
            ],
        }

        # Initialize quiz variables.
        self.current_question = 0
        self.score = 0
        self.total_questions = 0

        # Create a label for displaying the quiz question.
        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 14), bg="#581b61")

        # Create variables and buttons for quiz options.
        self.option_vars = []
        self.option_buttons = []

        # Create a button for moving to the next question.
        self.next_button = tk.Button(self.question_frame, text="Next", command=self.check_answer, bg="#581b61")

        # Create a label for displaying the quiz score.
        self.score_label = tk.Label(self.question_frame, text="", font=("Arial", 14), bg="#581b61")

        # Create a button for starting the quiz again.
        self.retry_button = tk.Button(self.question_frame, text="Start again", command=self.retry_quiz,
                                      bg="#581b61")

        # Initialize the quiz logic.
        self.question_logic()

        # Create a button for saving quiz results.
        self.save_button = tk.Button(self.question_frame, text="Save results", command=self.save_to_file,
                                     fg="black", bg="yellow")
        self.save_button.pack()

    def question_logic(self):
        # Display the category selection label and buttons.
        self.category_label.pack(pady=20)
        for category in self.categories:
            # Create buttons for each category and associate a callback function to select a category.
            button = tk.Button(root, text=category, command=lambda c=category: self.select_category(c),
                               fg="black", bg="yellow")
            button.pack()
            self.category_buttons.append(button)

        # Create a frame for quiz questions and answers.
        self.question_frame = tk.Frame(root, bg="#581b61")

        # Create a label for displaying quiz questions.
        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 14),
                                       fg="yellow", bg="#581b61")
        self.question_label.pack(pady=20)

        # Create option buttons for quiz answers. The amount of questions allowed
        self.option_buttons = []
        for i in range(10):
            var = tk.StringVar()
            var.set("")
            self.option_vars.append(var)

        for i in range(4):
            option_button = tk.Radiobutton(
                self.question_frame, text="", value="", font=("Arial", 12), bg="yellow")
            option_button.pack()
            self.option_buttons.append(option_button)

        next_button_frame = tk.Frame(self.question_frame, bg="#581b61")
        next_button_frame.pack(pady=10)

        # Create a button to move to the next question.
        self.next_button = tk.Button(self.question_frame, text="Next", command=self.check_answer,
                                     fg="black", bg="yellow")
        self.next_button.pack()

        # Create a label for displaying the quiz score.
        self.score_label = tk.Label(self.question_frame, text="", font=("Arial", 14),
                                    fg="yellow", bg="#581b61")
        self.score_label.pack(pady=20)

        # Create a button to start the quiz again.
        self.retry_button = tk.Button(self.question_frame, text="Start again  \r",
                                      fg="black", bg="yellow", command=self.retry_quiz)
        self.retry_button.pack_forget()

        # Create a button for saving quiz results and hide it initially.
        self.save_button = tk.Button(self.question_frame, text="Save results\r",
                                     fg="black", bg="yellow", command=self.save_to_file)
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
                # Display the current question number and the quiz question.
                question_data = self.questions[self.selected_category][self.current_question]
                question_number = self.current_question + 1
                self.question_label.config(
                    text=f"{question_number}/{self.total_questions}: {question_data['question']}")
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
        score_text = f"Thank you so much for playing\r" \
                     f" you got {self.score}/{self.total_questions} correct answers"
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
    root.geometry('500x260')
    root.title("Quiz")
    # Disable window resizing.
    root.resizable(False, False)
    # Start the GUI event loop.
    root.mainloop()
