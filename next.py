import tkinter as tk
import random

# Create the main tkinter window
root = tk.Tk()
root.geometry('425x300')
root.title("Quiz GUI")
root.resizable(False, False)


# Define a function to handle "Next" button clicks
def next_question():
    # Get the next question and its answers
    global current_question_index
    current_question_index += 1

    if current_question_index < len(questions):
        question_label.config(text=questions[current_question_index]["question"])
        answer_var.set(None)  # Clear the selected answer
        random.shuffle(questions[current_question_index]["answers"])  # Shuffle the answer choices
        for i in range(4):
            answer_buttons[i].config(text=questions[current_question_index]['answers'][i])

    else:
        question_label.config(text="Quiz completed!")


# Define a function to handle radio button selections
def check_answer():
    selected_answer = answer_var.get()
    if selected_answer is not None:
        print("Selected answer:", selected_answer)


# Create a list of questions and answers
questions = [
    {
        "question": "The capital of New Zealand",
        "answers": ["Auckland", "Christchurch", "Wellington", "Dunedin"]
    },
    {
        "question": "What is 3 + 3?",
        "answers": ["6", "7", "8", "9"]
    },
    {
        "question": "What is 4 + 4?",
        "answers": ["7", "8", "9", "10"]
    },
    {
        "question": "What is 5 + 4?",
        "answers": ["7", "8", "9", "10"]
    },
    {
        "question": "What is the capital of France?",
        "answers": ["London", "Paris", "Berlin", "Madrid"],
    },
    {
        "question": "What is 2 + 2?",
        "answers": ["3", "4", "5", "6"],
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answers": ["Earth", "Mars", "Saturn", "Jupiter"],
    },
    {
        "question": "What ?",
        "answers": ["", "", "", ""],
    },
    {
        "question": "What colour is grass?",
        "answers": ["red", "White", "blue", "green"],
    },
]

# Shuffle the order of questions
random.shuffle(questions)

# Initialize the current question index
current_question_index = -1

# Create a label for the question
question_label = tk.Label(root, text="", font=('Arial', 14))
question_label.pack(pady=20)

# Create answer radio buttons
answer_var = tk.StringVar()
answer_buttons = []
for i in range(4):
    answer_button = tk.Radiobutton(
        root, text="", variable=answer_var, value=questions[current_question_index]['answers'][i], font=('Arial', 12))
    answer_buttons.append(answer_button)
    answer_button.pack(pady=5)

# Create a "Next" button to display the next question
next_button = tk.Button(root, text="Next", width=20, height=2, command=next_question)
next_button.pack(pady=10)

# Start with the first question
next_question()

# Start the tkinter main loop
root.mainloop()

# what I need from u is to, add the score, retry button, error message. To do this refer back to "This one"
