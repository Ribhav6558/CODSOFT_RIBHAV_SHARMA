import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Error! Division by zero"
            else:
                result = num1 / num2

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x200")
root.configure(background='lightblue')

# Create input fields
entry1 = tk.Entry(root, width=10)
entry1.pack(pady=10)
entry2 = tk.Entry(root, width=10)
entry2.pack(pady=10)

# Create operation selection
operation_var = tk.StringVar()
operation_var.set("+")
operations = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack(pady=10)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

# Create result label
result_label = tk.Label(root, text="Result:")
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()



