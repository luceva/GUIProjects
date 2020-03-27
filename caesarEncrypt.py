'''
Ante Lucev
Feb, 5, 2020

Implement a Caesar cipher which encrypts all lower and uppercase letters,
but leaves punctuation, numbers, and spaces alone.  Keep uppercase upper and lowercase lower.
Allow the user to type in a text box normal text, choose an encryption offset, click a button,
and display the encrypted result.  Allow the user to decrypt as well (a negative offset is fine to decrypt).
'''
from tkinter import *

master = Tk()
master.minsize(width=350, height=200)
master.configure(background="greenyellow")
encrypted = ""
offset = 0

def start():
    def clearWidgets():
        list = master.grid_slaves()
        for l in list:
            l.destroy()

    def encryption():
        def decryption():
            reset.destroy()
            dencrypted = ""
            for letter in encrypted:
                if letter.islower():
                    dencrypted += chr((ord(letter) - 97 + int(offset)) % 26 + 97)
                elif letter.isupper():
                    dencrypted += chr((ord(letter) - 65 + int(offset)) % 26 + 65)
                else:
                    dencrypted += letter
            l5 = Label(master, text="Decryption result:", font=('Calibri', 15), width=15, background="greenyellow")
            l5.grid(column=0, row=3, pady=20)
            dec_result = Label(master, text=dencrypted, font=('Calibri', 15), width=15, background="greenyellow")
            dec_result.grid(column=1, row=3, pady=20)
            reset2 = Button(master, text="New encryption", command=start, font=('Courier New', 10), width=20)
            reset2.grid(column=1, row=4, pady=10)

        global encrypted, offset
        encrypted = ""
        text = text_box.get()
        offset = offset_box.get()
        for letter in text:
            if letter.islower():
                encrypted += chr((ord(letter) - 97 - int(offset)) % 26 + 97)
            elif letter.isupper():
                encrypted += chr((ord(letter) - 65 - int(offset)) % 26 + 65)
            else:
                encrypted += letter

        clearWidgets()
        l3 = Label(master, text="Sent with offset " + offset + ":", font=('Calibri', 15), width=15, background="greenyellow")
        l3.grid(column=0, row=0, pady=(30, 20))
        input = Label(master, text=text, font=('Calibri', 15), width=15, background="greenyellow")
        input.grid(column=1, row=0, pady=(30, 20))
        l4 = Label(master, text="Encryption result:", font=('Calibri', 15), width=15, background="greenyellow")
        l4.grid(column=0, row=1, pady=(10,20))
        enc_result = Label(master, text=encrypted, font=('Calibri', 15), width=15, background="greenyellow")
        enc_result.grid(column=1, row=1, pady=(10,20))
        decrypt = Button(master, text="Decrypt", command=decryption, font=('Courier New', 10), width=20)
        decrypt.grid(column=1, row=2)
        reset = Button(master, text="New encryption", command=start, font=('Courier New', 10), width=20)
        reset.grid(column=1, row=3, pady=10)

    clearWidgets()
    l1 = Label(master, text="Enter a text:", font=('Calibri', 15), width=15, background="greenyellow")
    l1.grid(column=0, row=0, pady=(30,20))

    text_box = Entry(master, font=('Calibri', 15), width=15)
    text_box.grid(column=1, row=0, pady=(30,20))

    l2 = Label(master, text="Offset:", font=('Calibri', 15), background="greenyellow")
    l2.grid(column=0, row=1)

    offset_box = Entry(master, font=('Calibri', 15), width=15)
    offset_box.grid(column=1, row=1)

    encrypt = Button(master, text="Encrypt", command=encryption, font=('Courier New', 10), width=20)
    encrypt.grid(column=1,row=2,rowspan=2,pady=20)

start()

mainloop()