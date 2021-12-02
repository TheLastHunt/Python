from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title("Service Management System")
root.iconbitmap("rest_icon.ico")

p_width = 1024
p_height = 640

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

width_diff_div = int((screen_width - p_width) / 2)
height_diff_div = int((screen_height - p_height) / 2)

root.geometry(f"{p_width}x{p_height}+{width_diff_div}+{height_diff_div}")

#Basic Calculator

right_frame = Frame(root, bg="white", borderwidth=10)
right_frame.pack(side=RIGHT)

calc_screen = Entry(right_frame, width=50, borderwidth=5)
calc_screen.grid(row=0, column=0, columnspan=3)


def number_click(num):
    current = calc_screen.get()
    calc_screen.delete(0, END)
    calc_screen.insert(0, str(current) + str(num))

def clear_click():
    calc_screen.delete(0, END)

def add_click():
    num1 = calc_screen.get()
    global n1
    n1 = float(num1)
    calc_screen.delete(0, END)
    global sign
    sign = "+"

def sub_click():
    num1 = calc_screen.get()
    global n1
    n1 = float(num1)
    calc_screen.delete(0, END)
    global sign
    sign = "-"

def mult_click():
    num1 = calc_screen.get()
    global n1
    n1 = float(num1)
    calc_screen.delete(0, END)
    global sign
    sign = "*"

def div_click():
    num1 = calc_screen.get()
    global n1
    n1 = float(num1)
    calc_screen.delete(0, END)
    global sign
    sign = "/"
    

def equals_click():
    num2 = calc_screen.get()
    calc_screen.delete(0, END)
    n2 = float(num2)
    if sign == "+":
        calc_screen.insert(0, str(n1 + n2))
    elif sign == "-":
        calc_screen.insert(0, str(n1 - n2))
    elif sign == "*":
        calc_screen.insert(0, str(n1 * n2))
    elif sign == "/":
        calc_screen.insert(0, str(n1 / n2))


    

button_1 = Button(right_frame, text="1", padx=50, pady=16, borderwidth=5, command=lambda: number_click(1))
button_1.grid(row=3, column=0)
button_2 = Button(right_frame, text="2", padx=50, pady=16, borderwidth=5, command=lambda: number_click(2))
button_2.grid(row=3, column=1)
button_3 = Button(right_frame, text="3", padx=50, pady=16, borderwidth=5, command=lambda: number_click(3))
button_3.grid(row=3, column=2)
button_4 = Button(right_frame, text="4", padx=50, pady=16, borderwidth=5, command=lambda: number_click(4))
button_4.grid(row=2, column=0)
button_5 = Button(right_frame, text="5", padx=50, pady=16, borderwidth=5, command=lambda: number_click(5))
button_5.grid(row=2, column=1)
button_6 = Button(right_frame, text="6", padx=50, pady=16, borderwidth=5, command=lambda: number_click(6))
button_6.grid(row=2, column=2)
button_7 = Button(right_frame, text="7", padx=50, pady=16, borderwidth=5, command=lambda: number_click(7))
button_7.grid(row=1, column=0)
button_8 = Button(right_frame, text="8", padx=50, pady=16, borderwidth=5, command=lambda: number_click(8))
button_8.grid(row=1, column=1)
button_9 = Button(right_frame, text="9", padx=50, pady=16, borderwidth=5, command=lambda: number_click(9))
button_9.grid(row=1, column=2)
button_0 = Button(right_frame, text="0", padx=50, pady=16, borderwidth=5, command=lambda: number_click(0))
button_0.grid(row=4, column=0)

button_add = Button(right_frame, text="+", padx=50, pady=16, borderwidth=5, command=add_click)
button_add.grid(row=4, column=1)
button_subtract = Button(right_frame, text="-", padx=50, pady=16, borderwidth=5, command=sub_click)
button_subtract.grid(row=4, column=2)
button_multiply = Button(right_frame, text="x", padx=50, pady=16, borderwidth=5, command=mult_click)
button_multiply.grid(row=5, column=0)
button_divide = Button(right_frame, text="/", padx=50, pady=16, borderwidth=5, command=div_click)
button_divide.grid(row=5, column=1)

button_clear = Button(right_frame, text="CLEAR", padx=35, pady=16, borderwidth=5, command=clear_click)
button_clear.grid(row=5, column=2)

button_equals = Button(right_frame, text="=", padx=170, pady=16, borderwidth=5, command=equals_click)
button_equals.grid(row=6, column=0, columnspan=3)


#Item Selection Screen

left_frame = LabelFrame(root, bg="white", borderwidth=10)
left_frame.pack(side=LEFT)

total = 0

item_prices = {
    "GarlicBread":3.50,
    "Focaccia":2.50,
    "Pizza":9.00

}

def item_button_click(item, total):
    total += item_prices[item]
    


for item in item_prices.keys():
    Button_item = Button(left_frame, padx=50, pady=16, borderwidth=5, text=item, command=item_button_click(item, total))
    Button_item.pack(side=LEFT)

total_output = Entry(left_frame, width=100, borderwidth=5)
total_output.pack(side=BOTTOM)

def total_calc():
    total_output.delete(0, END)
    total_output.insert(0, total)

total_button = Button(left_frame, width=50, borderwidth=5, text="Total", command=total_calc)
total_button.pack(side=BOTTOM)

root.mainloop()