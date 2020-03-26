'''
Ante Lucev
Feb, 5, 2020
Program where the user can choose a counting up stopwatch:
Hit start, watch the numbers fly by, and hit stop and display the time.
'''

from tkinter import *
import numpy as geek

master = Tk()
master.minsize(width=350, height=250)
master.configure(background="aqua")

counter = 0
on = False

def count():
    if on:
        global counter
        if counter/60 < 10 and geek.mod(counter, 60) < 10:
            watch['text'] = "0" + str(int(counter/60)) + ":0" + str(geek.mod(counter, 60))
        elif (counter/60) < 10 and geek.mod(counter, 60) >= 10:
            watch['text'] = "0" + str(int(counter / 60)) + ":" + str(geek.mod(counter, 60))
        elif (counter/60) >= 10 and geek.mod(counter, 60) < 10:
            watch['text'] = str(int(counter / 60)) + ":0" + str(geek.mod(counter, 60))
        else:
            watch['text'] = str(int(counter / 60)) + ":" + str(geek.mod(counter, 60))

        master.after(1000, count)
        counter += 1

def startWatch():
    global on
    on = True
    count()
    start['state']='disabled'
    stop['state']='normal'
    restart['state']='normal'

def stopWatch():
    global on
    on = False
    start['state']='normal'
    stop['state']='disabled'
    restart['state']='normal'

def restartWatch():
    global counter
    global on
    counter = 0
    on = False
    watch['text'] = "00:0" + str(counter)
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    restart['state'] = 'disabled'

watch = Label(master, text="00:0" + str(counter), font=('Courier New', 50), width=10, background="aqua")
watch.grid()

start = Button(master,text="Start the stopwatch", command = startWatch, font=('Courier New', 10), width=25, height=2)
start.grid(column=0,row=1)

stop = Button(master,text="Stop the stopwatch", state='disabled', command = stopWatch, font=('Courier New', 10), width=25, height=2)
stop.grid(column=0,row=2,pady=5)

restart = Button(master,text="Restart the stopwatch", state='disabled', command = restartWatch, font=('Courier New', 10), width=25, height=2)
restart.grid(column=0,row=3)

mainloop()
