#SPELLING CHECKER APP USING Tkinter & TextBlob
# Install textblop using: pip install textblob
import tkinter
from tkinter import *
from textblob import TextBlob

root=Tk()
root.title("Spelling Checker App")
root.geometry("800x400")
root.config(background="#0d0c07")

def check_spelling():
    word=input_text.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs=Label(root,text="Correct spelling is :",font=("poppins",20),bg="#0d0c07",fg="#e0e1dc")
    cs.place(x=100,y=250)
    spell.config(text=right)

heading= Label(root,text="Spelling Checker",font=("ariel",30,"bold"),bg="#0d0c07",fg="#e0e1dc")
heading.pack(pady=(50,0))

input_text=Entry(root,justify="center",width=20,font=("ariel",30),bg="white",border=2)
input_text.pack(pady=10)
input_text.focus()

button=Button(root,text="Check",font=("arial",20,"bold"),fg="white",bg="blue",command=check_spelling)
button.pack()

spell=Label(root,font=("poppins",20),bg="#0d0c07",fg="#e0e1dc")
spell.place(x=350,y=250)

root.mainloop()