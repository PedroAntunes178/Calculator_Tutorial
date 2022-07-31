#! /usr/bin/env python3
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

DEBUG = 0
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
    if DEBUG: print(numbers)
    if DEBUG: print(operations)
    for i in range(len(operations)):
        numbers[i+1] = do_operation(numbers[i], numbers[i+1], operations[i])
    return numbers[-1]

def calculate(calc):
    if DEBUG: print('Expression to calculate: ' + calc)
    input_numbers    = list()
    input_operations = list()
    possible_operations = ['+', '-', '/', '*']
    aux = ''
    idx = 0
    while (idx < len(calc)):
        c = calc[idx]
        if (c == '('):
            if (aux != ''):
                input_numbers.append(float(aux))
                input_operations.append('*')
                aux = ''
            i_idx_subcalc = calc.find('(')+1
            f_idx_subcalc = calc.rfind(')')
            if DEBUG: print('Sub calculation between ' + str(i_idx_subcalc) + ' and ' + str(f_idx_subcalc))
            aux = calculate(calc[i_idx_subcalc:f_idx_subcalc])
            idx = f_idx_subcalc
        elif (c in possible_operations):
            input_numbers.append(float(aux))
            input_operations.append(c)
            aux = ''
        else:
            aux += c
        idx = idx + 1
    input_numbers.append(float(aux))
    if DEBUG: print(input_numbers)
    if DEBUG: print(input_operations)
    res = do_calc(input_numbers, input_operations)
    if DEBUG: print(int(res))
    return str(res)

def print_calculator():
    i = 0
    button = list()
    possible_button = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')']
    while (i < len(possible_button)):
        button.append(tk.Button(master=frame, text=possible_button[i], padx=15, pady=5, width=3, command=lambda key=possible_button[i]: myclick(key)))
        button[i].grid(row=int(1+i/3), column=i%3, pady=2)
        i = i + 1
    button_clear = tk.Button(master=frame, text="clear", padx=15, pady=5, width=6, command=clear)
    button_clear.grid(row=int(2+i/3), column=0, columnspan=2, pady=2)
    button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, width=6, command=equal)
    button_equal.grid(row=int(2+i/3), column=1, columnspan=2, pady=2)

print_calculator()
window.mainloop()
