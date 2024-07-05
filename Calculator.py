import tkinter as tk
from tkinter import messagebox


# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror('Error', 'Invalid Input')


# Function to add a character to entry field
def button_click(char):
    entry.insert(tk.END, char)


# Function to clear entry field
def clear():
    entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title('Calculator')

# Entry widget to display input/output
entry = tk.Entry(root, width=20, font=('Arial', 20), bd=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons and their positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0), ('.', 4, 1), ('e', 4, 2),
]

op = [
    ('/', 1, 3), ('*', 2, 3), ('-', 3, 3), ('+', 4, 3),
    ('%', 5, 0), ('(', 5, 1), (')', 5, 2)
]

# Create buttons with colors and positions
for (text, row, column) in buttons:
    btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 15), bd=5,
                    command=lambda char=text: button_click(char))
    btn.grid(row=row, column=column, padx=5, pady=5)

for (text, row, column) in op:
    btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 15), fg="white", bg="dark blue", bd=5,
                    command=lambda char=text: button_click(char))
    btn.grid(row=row, column=column, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text='Clear', width=5, height=2, font=('Arial', 15),fg="white", bg="maroon", bd=5, command=clear)
clear_btn.grid(row=6, column=3, columnspan=2, padx=5, pady=5)

# Equals button
equal_btn = tk.Button(root, text='=', width=5, height=2, font=('Arial', 15), bd=5, bg="red", fg="White", command=evaluate)
equal_btn.grid(row=5, column=3, columnspan=2, padx=5, pady=5)

# Run the main loop
root.mainloop()
