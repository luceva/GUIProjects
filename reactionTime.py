'''
Ante Lucev
Feb, 5, 2020

Create some game where the user must click something in reaction
to a change on the screen to measure their reaction time.
Present the time and allow the player to try again.
'''
from tkinter import *
import random
from time import time as the_timer

master = Tk()
master.minsize(width=300, height=200)
master.configure(background="skyblue")
rand = 0
start_time = 0

def clearWidgets():
    list = master.grid_slaves()
    for l in list:
        l.destroy()

def startGame():
    global master, rand, start_time

    clearWidgets()
    def colorChange():
        master.configure(background="red")
        l1.configure(background="red")

    start_time = the_timer()
    master.configure(background="royalblue")
    l1 = Label(master, text="Click stop when you see red!", font=('Calibri', 15), background="royalblue")
    l1.grid(column=0, row=0, pady=(40,20))
    stop = Button(master, text="Stop", command=stopGame, font=('Courier New', 10), width=20)
    stop.grid(column=0, row=1, padx=115)
    rand = random.randint(2500, 7500)
    master.after(rand, colorChange)

def stopGame():
    clearWidgets()
    end_time = the_timer()
    total = round((end_time - start_time) - (rand/1000),3)
    l2 = Label(master, text="Your reaction in sec:", font=('Calibri', 15), width=20, background="red")
    l2.grid(column=0, row=0, pady=(40,20))
    time = Label(master, text=total, font=('Calibri', 15), width=20, background="red")
    time.grid(column=1, row=0, pady=(40,20))
    rest = Button(master, text="Try again", command=startGame, font=('Courier New', 10), width=20)
    rest.grid(column=0,row=1,columnspa=2)

start = Button(master,text="Start the game", command = startGame, font=('Courier New', 10), width=20)
start.grid(column=0,row=0,padx=115,pady=75)

mainloop()