import tkinter as tk
import math

def plus(a, b):
    return float(a + b)

def minus(a, b):
    return float(a - b)

def mul(a, b):
    return float(a * b)

def div(a, b):
    return float(a / b)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def floor(a):
    return math.floor(a)

def ceil(a):
    return math.ceil(a)

def mod(a, b):
    return a % b

def calculate(entry1, entry2, dropdown, result_label):
    try:
        num1 = float(entry1.get())
        operation = dropdown.get()

        if operation in ['sin', 'cos', 'floor', 'ceil']:
            entry2.config(state='disabled')
            num2 = None
        else:
            entry2.config(state='normal')
            num2 = float(entry2.get())

        if operation == '/' and num2 == 0:
            result_label.config(text="Ошибка, нельзя делить на 0")
            return

        result = perform_calculation(num1, num2, operation)
        result_label.config(text="Результат: " + str(result))
    except ValueError:
        result_label.config(text="Непредвиденная ошибка")

def perform_calculation(num1, num2, operation):
    if operation == '+':
        return plus(num1, num2)
    elif operation == '-':
        return minus(num1, num2)
    elif operation == '*':
        return mul(num1, num2)
    elif operation == '/':
        return div(num1, num2)
    elif operation == 'sin':
        return sin(num1)
    elif operation == 'cos':
        return cos(num1)
    elif operation == 'floor':
        return floor(num1)
    elif operation == 'ceil':
        return ceil(num1)
    elif operation == 'mod':
        return mod(num1, num2)
    else:
        return "Ошибка"

def on_dropdown_change(entry2, dropdown):
    operation = dropdown.get()
    if operation in ['sin', 'cos', 'floor', 'ceil']:
        entry2.delete(0, tk.END)
        entry2.config(state='disabled')
    else:
        entry2.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Калькулятор")
    root.geometry("400x200")

    entry1 = tk.Entry(root, width=20)
    entry1.pack()
    entry2 = tk.Entry(root, width=20)
    entry2.pack()

    dropdown = tk.StringVar(root)
    dropdown.set('+')
    options = ['+', '-', '*', '/', 'sin', 'cos', 'floor', 'ceil', 'mod']
    dropdown.trace('w', lambda *args: on_dropdown_change(entry2, dropdown))
    dropdown_menu = tk.OptionMenu(root, dropdown, *options)
    dropdown_menu.pack()

    calculate_button = tk.Button(root, text="Calculate", command=lambda: calculate(entry1, entry2, dropdown, result_label))
    calculate_button.pack()

    result_label = tk.Label(root, text="Result:")
    result_label.pack()

    root.mainloop()
