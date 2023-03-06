import tkinter
from tkinter import *

root=Tk()
root.title("Gui Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#07366e")

label_result =Label(root,width=25,height=2,text="",font=("ariel",30))
label_result.pack()

Button(root,text="C", width=5, height=1,font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=10,y=100)

root.mainloop()