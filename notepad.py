# NOTEPAD GUI IN PYTHON using Tkinter
from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("600x600")
root.title("Notepad")
root.config(bg='#2e1f0c')
root.resizable(False,False)

def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)

entry=Text(root,height='33',width='72',wrap=WORD)
entry.place(x=10,y=60)

b1=Button(root,width='20',height='2',bg='#f5f4f2',text='save_file',command=save_file).place(x=100,y=5)
b2=Button(root,width='20',height='2',bg='#f5f4f2',text='open_file',command=open_file).place(x=300,y=5)

root.mainloop()
