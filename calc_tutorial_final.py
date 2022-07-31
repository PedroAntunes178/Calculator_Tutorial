import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

PROGRAM = 'Calculator Tutorial'
window_width = 10

window = tk.Tk()
window.title(PROGRAM)
frame = tk.Frame(master=window, bg="skyblue", padx=window_width)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

def myclick(number):
    entry.insert(tk.END, number)

def equal():
    try:
        y = str(calculate(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

def do_operation(x, y, operation):
    if(operation == '+'):
        return x+y
    elif(operation == '-'):
        return x-y
    elif(operation == '*'):
        return x*y
    elif(operation == '/'):
        return x/y

def do_priority_calc(numbers, operations):
    tmp_numbers = []
    tmp_operations = []
    priority_operations = ['*', '/']
    for i in range(len(operations)):
        if(operations[i] in priority_operations):
            numbers[i+1] = do_operation(numbers[i], numbers[i+1], operations[i])
        else:
            tmp_numbers.append(numbers[i])
            tmp_operations.append(operations[i])
    tmp_numbers.append(numbers[-1]) # numbers[-1] = numbers[len(operations)]
    return tmp_numbers, tmp_operations

def do_calc(numbers, operations):
    numbers, operations = do_priority_calc(numbers, operations)
    print(numbers)
    print(operations)
    for i in range(len(operations)):
        numbers[i+1] = do_operation(numbers[i], numbers[i+1], operations[i])
    return numbers[-1]

def calculate(calc):
    input_numbers    = list()
    input_operations = list()
    possible_operations = ['+', '-', '/', '*']
    aux = ''
    for c in calc:
        if (c in possible_operations):
            input_numbers.append(float(aux))
            input_operations.append(c)
            aux = ''
        else:
            aux += c
    input_numbers.append(float(aux))
    print(input_numbers)
    print(input_operations)
    res = do_calc(input_numbers, input_operations)
    print(int(res))
    return res

def print_calculator():
    button = list()
    possible_button = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']
    for i in range(len(possible_button)):
        button.append(tk.Button(master=frame, text=possible_button[i], padx=15, pady=5, width=3, command=lambda key=possible_button[i]: myclick(key)))
        button[i].grid(row=int(1+i/3), column=i%3, pady=2)

    button_clear = tk.Button(master=frame, text="clear",
                             padx=15, pady=5, width=6, command=clear)
    button_clear.grid(row=6, column=0, columnspan=2, pady=2)

    button_equal = tk.Button(master=frame, text="=", padx=15,
                             pady=5, width=6, command=equal)
    button_equal.grid(row=6, column=1, columnspan=2, pady=2)

print_calculator()
window.mainloop()
