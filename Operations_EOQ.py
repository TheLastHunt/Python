from tkinter import *
import math

root = Tk()
root.title("EOQ and TC calculator")

demand = Label(root, text="Enter Demand(D) Value:")
demand.grid(row=0, column=0)
demand_entry = Entry(root, width=50, borderwidth=5)
demand_entry.grid(row=1, column=0)

quantity = Label(root, text="Enter Quantity(Q) Value:")
quantity.grid(row=3, column=0)
quantity_entry = Entry(root, width=50, borderwidth=5)
quantity_entry.grid(row=4, column=0)

fixed = Label(root, text="Enter Fixed Cost per Order(K) Value:")
fixed.grid(row=6, column=0)
fixed_entry = Entry(root, width=50, borderwidth=5)
fixed_entry.grid(row=7, column=0)

holding = Label(root, text="Enter Holding Cost(h) Value:")
holding.grid(row=9, column=0)
holding_entry = Entry(root, width=50, borderwidth=5)
holding_entry.grid(row=10, column=0)

cost = Label(root, text="Enter Unit Cost(c) Value:")
cost.grid(row=12, column=0)
cost_entry = Entry(root, width=50, borderwidth=5)
cost_entry.grid(row=13, column=0)

tc_result = Label(root, text="Result for Total Costs:")
tc_result.grid(row=17, column=0)
result_screen = Entry(root)
result_screen.grid(row=19, column=0)

eoq_result = Label(root, text="Result for EOQ:")
eoq_result.grid(row=21, column=0)
result_screen_2 = Entry(root)
result_screen_2.grid(row=23, column=0)

def calc_tc_eoq():
    fixed_c = float(demand_entry.get()) / float(quantity_entry.get()) * float(fixed_entry.get())
    holding_c = float(quantity_entry.get()) / 2 * float(holding_entry.get())
    production_c = float(cost_entry.get()) * float(demand_entry.get())
    tc = fixed_c + holding_c + production_c
    result_screen.delete(0, END)
    result_screen.insert(0, float(tc))

    eoq = math.sqrt(2 * float(fixed_entry.get()) * float(demand_entry.get()) / float(holding_entry.get()))
    result_screen_2.delete(0, END)
    result_screen_2.insert(0, float(eoq))


calc_button = Button(root, text="Calculate TC and EOQ", command=calc_tc_eoq)
calc_button.grid(row=15, column=0)


root.mainloop()