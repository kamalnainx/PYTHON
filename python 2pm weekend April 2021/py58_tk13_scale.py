# from tkinter import *

# top = Tk()

# top.geometry("300x300")

# scale=Scale(top, variable=DoubleVar(), from_=1, to=100, orient=HORIZONTAL)
# scale.pack(anchor=W)

# top.mainloop()







































from tkinter import *

def select():
    sel="Value = "+str(v.get())
    label.config(text=sel)

top = Tk()

top.geometry("300x300")
v=DoubleVar()

scale=Scale(top, variable=v, from_=1, to=100, orient=HORIZONTAL)
scale.pack(anchor=CENTER)

btn=Button(top, text="Value", command=select)
btn.pack(anchor=CENTER)

label=Label(top)
label.pack()
top.mainloop()

