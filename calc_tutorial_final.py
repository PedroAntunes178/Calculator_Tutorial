#! /usr/bin/env python3
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
from calc_tutorial_5 import *

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
