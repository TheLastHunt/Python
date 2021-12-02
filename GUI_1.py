from tkinter import *

root = Tk()

#Creating Label Widget
#my_label1 = Label(root, text="Hello World!")
#my_label2 = Label(root, text="I'm Zezão Bonzão!")


#Shoving it onto the screen -> pack
#Grid system -> grid
#my_label1.grid(row=0, column=0)
#my_label2.grid(row=1, column=0)

#Buttons
#padx/pady for size, fg for font color, bg for background color
def clicked_the_button():
    new_label = Label(root, text=ent.get())
    new_label.pack()

my_button = Button(root, text="Enter name:", command=clicked_the_button)
my_button.pack()

#Input Boxes
#width, bg, fg, borderwidth, get, insert
ent = Entry(root, width=50, borderwidth=5)
ent.pack()
ent.insert(0, "Enter name here")

root.mainloop()