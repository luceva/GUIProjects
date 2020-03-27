'''
Ante Lucev
Feb, 5, 2020

At the beginning of many board games a random person must be chosen to go first.
This program should allow the user to enter a list of names in a box, separated by newlines, press a ‘Pick Player’ button,
and a random name is displayed.  Every time the button is clicked a different name is chosen.
It should never pick the same name twice in succession.
'''
from tkinter import *
import random

master = Tk()
master.minsize(width=750, height=150)
master.configure(background="orangered")
previous = ""

def names():
    global previous
    string_name = names_box.get()
    list_name = string_name.split()
    name = random.choice(list_name)
    while(name == previous):
        name = random.choice(list_name)
    previous = name
    label1 = Label(master, text="Result:", font=('Calibri', 15), width=20, background="orangered")
    label1.grid(column=0, row=2,sticky=E,pady=20)
    result = Label(master, text=name, font=('Calibri', 15), width=20, background="orangered")
    result.grid(column=1, row=2)

label1 = Label(master, text="Enter a list of names:", font=('Calibri', 15), width=20, background="orangered")
label1.grid(column=0, row=0,columnspan=2,sticky=W,padx=10,pady=15)

names_box = Entry(master, font=('Calibri', 15), width=50)
names_box.grid(column=0, row=1,padx=10)

submit = Button(master, text="Pick Player", command=names, font=('Courier New', 10), width=20)
submit.grid(column=1,row=1)

mainloop()