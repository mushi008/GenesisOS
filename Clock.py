import os
from tkinter import *
from tkinter.ttk import *
from time import strftime
from tkinter import font

root = Tk()
root.title("Clock")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("Helvetica", 80), background="Black", foreground="Cyan")
label.pack(anchor='center')
time()

mainloop()
