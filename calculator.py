import sys, os
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

root = ThemedTk(theme='yaru')
root.resizable(width=False, height=False)
root.title('My Calculator')
root.iconbitmap(r"E:\GB\PY_projects\pythonProject\calculator\calculator.ico")

e = ttk.Entry(root, width=48,)
e.grid(row=0, column=0, columnspan=4, padx=4, pady=4)
e.focus_set()


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_plus():
    first_number = e.get()
    global f_num
    global math
    math = "plus"
    f_num = int(first_number)
    e.delete(0, END)


def button_minus():
    first_number = e.get()
    global f_num
    global math
    math = "minus"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "plus":
        e.insert(0, f_num + int(second_number))
    if math == "minus":
        e.insert(0, f_num - int(second_number))
    if math == "multiply":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))


button_1 = ttk.Button(root, text='1', command=lambda: button_click(1))
button_2 = ttk.Button(root, text='2', command=lambda: button_click(2))
button_3 = ttk.Button(root, text='3', command=lambda: button_click(3))
button_4 = ttk.Button(root, text='4', command=lambda: button_click(4))
button_5 = ttk.Button(root, text='5', command=lambda: button_click(5))
button_6 = ttk.Button(root, text='6', command=lambda: button_click(6))
button_7 = ttk.Button(root, text='7', command=lambda: button_click(7))
button_8 = ttk.Button(root, text='8', command=lambda: button_click(8))
button_9 = ttk.Button(root, text='9', command=lambda: button_click(9))
button_0 = ttk.Button(root, text='0', command=lambda: button_click(0))

button_plus = ttk.Button(root, text="+", command=button_plus)
button_minus = ttk.Button(root, text='-', command=button_minus)
button_multiply = ttk.Button(root, text='*', command=button_multiply)
button_division = ttk.Button(root, text='/', command=button_divide)
button_equal = ttk.Button(root, text='=', command=button_equal)

button_clear = ttk.Button(root, text='C', command=button_clear)

button_1.grid(row=3, column=0, ipady=10)
button_2.grid(row=3, column=1, ipady=10)
button_3.grid(row=3, column=2, ipady=10)


button_4.grid(row=2, column=0, ipady=10)
button_5.grid(row=2, column=1, ipady=10)
button_6.grid(row=2, column=2, ipady=10)

button_7.grid(row=1, column=0, ipady=10)
button_8.grid(row=1, column=1, ipady=10)
button_9.grid(row=1, column=2, ipady=10)

button_0.grid(row=4, column=1, ipady=10)

button_clear.grid(row=4, column=0, ipady=10)
button_plus.grid(row=3, column=3, ipady=10)
button_minus.grid(row=2, column=3, ipady=10)
button_multiply.grid(row=1, column=3, ipady=10)
button_division.grid(row=4, column=2, ipady=10)
button_equal.grid(row=4, column=3, ipady=10)

root.mainloop()
