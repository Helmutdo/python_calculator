""" calculator with GUI"""
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk

# function to perform addition
def add(num1, num2, result_var):
    result = num1 + num2
    result_var.set(result)
    messagebox.showinfo("Result", f"The result is: {result}")

# function to perform substraction
def substract(num1, num2, result_var):
    result = num1 - num2
    result_var.set(result)
    messagebox.showinfo("Result", f"The result is: {result}")

# function to perform multiplication
def multiply(num1, num2, result_var):
    result = num1 * num2
    result_var.set(result)
    messagebox.showinfo("Result", f"The result is: {result}")

# function to perform division 
def divide(num1, num2, result_var):
    try:
        result = num1 / num2
        result_var.set(result)
        messagebox.showinfo("Result", f"The result is: {result}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        result_var.set("undefined")

# function to get uset input and perform the selected operation
def calculate(operation, result_var):
    try:
        num1 = float(simpledialog.askstring("Input", "Enter the first number: "))
        num2 = float(simpledialog.askstring("Input", "Enter the second number: "))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only. ")
        return
    if operation == "Add":
        add(num1, num2, result_var)
    elif operation == "Substract":
        substract(num1, num2, result_var)
    elif operation == "Multiply":
        multiply(num1, num2, result_var)
    elif operation == "Divide":
        divide(num1, num2, result_var)
    else:
        messagebox.showerror("Error", "Invalid operation. Please try again.")
        return
    result_var.set("")
    messagebox.showinfo("Result", f"The result is: {result_var.get()}")

# function to create the GUI
def create_gui():
    root = tk.Tk()
    root.title("Unconfortable Calculator")
    root.geometry("400x300")
    root.resizable(False, False)
    root.configure(bg="lightblue")
    
    # create a label for the title
    title_label = tk.Label(root, text="Simple Calculator", font=("Arial", 16), bg="lightblue")
    title_label.pack(pady=10)
    
    # create a label for the result
    result_var = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14), bg="lightblue")
    result_label.pack(pady=10)
    
    # create a frame for the buttons
    button_frame = ttk.Frame(root)
    button_frame.pack(pady=10)
    
    # create butttons for each operation
    add_button = ttk.Button(button_frame, text="Add", command = lambda : calculate("Add", result_var))
    add_button.grid(row=0,column=0, padx=5, pady=5)
    substract_button = ttk.Button(button_frame, text="Substract", command= lambda : calculate("Substract", result_var))
    substract_button.grid(row=0, column=1, padx=5, pady=5)
    multiply_button = ttk.Button(button_frame, text= "Multiple", command= lambda: calculate("Multiply", result_var))
    multiply_button.grid(row=0, column=2, padx=5, pady=5)
    divide_button = ttk.Button(button_frame, text = "Dvide", command= lambda: calculate("Divide", result_var))
    divide_button.grid(row=0, column=3, padx=5, pady=5)
    
    # create a button to exit the app
    exit_button = ttk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=10)
    
    # start the main loop
    root.mainloop()

# main function to run the GUI - constructor
if __name__ == "__main__":
    create_gui()
        # create the GUI