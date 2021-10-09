from tkinter import *

top=Tk()

top.geometry("300x200")

def select():
    sel="Value"+str(v.get())
    labelselection1.config(text=sel)

v=DoubleVar()
scale1=Scale(top,variable=v, from_=1, to =100, orient=HORIZONTAL)
scale1.pack(anchor=CENTER)

button1=Button(top,text="select value",command=select)
button1.pack(anchor=CENTER)

labelselection1=Label(top)
labelselection1.pack()
top.mainloop()
