# import tkinter
# from tkinter import *

# top=Tk()
# top.geometry("300x300")

# lf1=LabelFrame(top,text="!st labelframe")
# lf1.pack(fill="both", expand="yes")

# top.mainloop()







































# import tkinter
# from tkinter import *

# top=Tk()
# top.geometry("300x300")

# lf1=LabelFrame(top,text="1st labelframe")
# lf1.pack(fill="both", expand="yes")

# lf2=LabelFrame(top,text="2st labelframe")
# lf2.pack(fill="both", expand="yes")

# top.mainloop()





































import tkinter
from tkinter import *

top=Tk()
top.geometry("300x300")

lf1=LabelFrame(top,text="1st labelframe")
lf1.pack(fill="both", expand="yes")

toplabel=Label(lf1, text="this is my top label")
toplabel.pack()

lf2=LabelFrame(top,text="2st labelframe")
lf2.pack(fill="both", expand="yes")

bootmlabel=Label(lf2, text="this is my bottem label")
bootmlabel.pack()

top.mainloop()




