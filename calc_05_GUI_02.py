"""Classic calculator with GUI mimicking a real calculator"""

import tkinter as tk
from tkinter import messagebox

# Function to perform addition
def add(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiply(num1, num2):
    return num1 * num2

# Function to perform division
def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        return "undefined"

# Function to get user input and perform the selected operation
def calculate(operation, num1, num2):
    if operation == "Add":
        return add(num1, num2)
    elif operation == "Subtract":
        return subtract(num1, num2)
    elif operation == "Multiply":
        return multiply(num1, num2)
    elif operation == "Divide":
        return divide(num1, num2)
    else:
        messagebox.showerror("Error", "Invalid operation. Please try again.")
        return None

# Function to handle button clicks
def button_click(value):
    current_text = display.get()
    if value == "C":
        display.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(current_text)
            display.delete(0, tk.END)
            display.insert(0, result)
        except Exception:
            messagebox.showerror("Error", "Invalid input.")
    elif value == "Exit":
        root.quit()
    else:
        display.insert(tk.END, value)

# Function to create the GUI
def create_gui():
    global root, display
    root = tk.Tk()
    root.title("The Real Calculator")
    root.geometry("400x600")
    root.configure(bg="black")
    root.resizable(0, 0)

    # Try setting the icon, but don't crash if the file is missing
    try:
        root.iconbitmap("calculator.ico")
    except:
        pass  # Continue execution even if icon is missing

    display = tk.Entry(root, font=("Arial", 24), bd=10, insertwidth=2, borderwidth=4, justify="right")
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Create the buttons
    buttons = [
        ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
        ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
        ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("/", 4, 3),
        ("Exit", 5, 0)
    ]

    for (text, row, col) in buttons:
        button = tk.Button(root, text=text, width=5, height=2, bg="black", fg="white", font=("Arial", 20),
                           command=lambda t=text: button_click(t))
        button.grid(row=row, column=col, padx=5, pady=5)

    root.mainloop()

# Construct to run the code
if __name__ == "__main__":
    create_gui()
