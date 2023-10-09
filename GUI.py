import tkinter as tk

# Create the main tkinter window
root = tk.Tk()
root.geometry('425x300')
root.title("Quiz GUI")
root.resizable(False, False)


# Define a function to handle button clicks
def check_answer():
    selected_answer = answer_var.get()
    print("Selected answer:", selected_answer)


# Create a label for the question
question_label = tk.Label(root, text="What is 2 + 2?", font=('Arial', 14))
question_label.pack(pady=20)

# Create answer radio buttons
answer_var = tk.StringVar()
answer_buttons = []
for answer_text in ["3", "4", "5", "6"]:
    answer_button = tk.Radiobutton(root, text=answer_text, variable=answer_var, value=answer_text,
                                   font=('Arial', 12))
    answer_buttons.append(answer_button)
    answer_button.pack(pady=5)

# Create a Submit button to check the answer
submit_button = tk.Button(root, text="Next", width=20, height=2, command=check_answer)
submit_button.pack(pady=10)

# There is now a submit button with radio buttons, ensured one answer, and you can't tick multiple
# Start the tkinter main loop
root.mainloop()
