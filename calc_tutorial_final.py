#! /usr/bin/env python3
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
from calc_tutorial_5 import *

PROGRAM = 'Calculator Tutorial'
W_WIDTH = 6
N_COL = 4

window = tk.Tk()
frame = tk.Frame(master=window, bg="skyblue", padx=W_WIDTH)
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=N_COL, width=N_COL*W_WIDTH)

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
        button.append(tk.Button(master=frame, text=possible_button[i], padx=W_WIDTH*N_COL/2, pady=W_WIDTH/2, width=N_COL, command=lambda key=possible_button[i]: myclick(key)))
        button[i].grid(row=int(1+i/N_COL), column=i%N_COL, pady=2)
        i = i + 1
    button_clear = tk.Button(master=frame, text="clear", padx=W_WIDTH*N_COL/2, pady=W_WIDTH/2, width=N_COL*2, command=clear)
    button_clear.grid(row=int(2+i/N_COL), column=0, columnspan=2, pady=2)
    button_equal = tk.Button(master=frame, text="=", padx=W_WIDTH*N_COL/2, pady=W_WIDTH/2, width=N_COL*2, command=equal)
    button_equal.grid(row=int(2+i/N_COL), column=2, columnspan=2, pady=2)

def init_gui():
    window.title(PROGRAM)
    window.resizable(False,False)
    window.bind('<Return>',lambda event:equal())
    frame.pack()
    entry.grid(row=0, column=0, columnspan=N_COL, ipady=2, pady=2)

init_gui()
print_calculator()
window.mainloop()
