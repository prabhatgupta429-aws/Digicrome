import tkinter as tk

# Function to update the expression in the entry widget
def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(symbol))

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Creating the main window
calculator_object = tk.Tk()
calculator_object.title("Simple Calculator")

calculator_object.config(bg="yellow")
# Entry widget to display the expression
entry = tk.Entry(calculator_object, width=30, font=('Arial', 20), bg="white")
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons for the calculator in
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]


# Clear button C to clear all text/expressions
tk.Button(calculator_object, text='C', width=40, font=('Arial', 14), fg="Red", bg="lavender", command=clear_entry).grid(row=1, column=0, columnspan=4)

# Add buttons to the grid of the calculator
row_val = 2
col_val = 0
for button in buttons:
    tk.Button(calculator_object, text=button, padx=20, pady=20, font=('Arial', 14), fg="Red", bg="aliceblue",
              command=lambda symbol=button: button_click(symbol) if symbol != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


# Run the Tkinter event loop
calculator_object.mainloop()