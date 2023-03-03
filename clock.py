from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title("Clock")

def present_time():
    display_time = time.strftime("%H:%M:%S %p")
    digital_clock.config(text=display_time)
    digital_clock.after(200,present_time)

digital_clock = Label(root, font=("arial",150),bg="blue",fg="black")
digital_clock.pack()

present_time

root.mainloop()
"""
from tkinter import *
from tkinter.ttk import *

root = Tk()
label = Label(root, text ="No kugeria mani!")
label.pack()
root.mainloop()
"""