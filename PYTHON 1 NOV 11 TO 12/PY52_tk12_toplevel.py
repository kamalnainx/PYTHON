from tkinter import *

root=Tk()

root.geometry("300x200")

def open():
    top1=Toplevel(root)
    top.mainloop()

button1=Button(root,text="open top level", command=open)
button1.place(x=100,y=100)

root.mainloop()
