##from tkinter import *
##
##top=Tk()
##
##top.geometry("300x300")
##
####checkvar1=IntVar()
##
##checkbutton1=Checkbutton(top, text='c', variable=IntVar(), onvalue=1, offvalue=0, height=2, width=2)
##checkbutton1.pack()
##top.mainloop()








from tkinter import *

top=Tk()
top.geometry("300x300")

checkbutton1=Checkbutton(top, text='c', variable=IntVar(), onvalue=1, offvalue=0, height=2, width=2)
checkbutton1.pack()

checkbutton2=Checkbutton(top, text='c++', variable=IntVar(), onvalue=1, offvalue=0, height=2, width=2)
checkbutton2.pack()

checkbutton3=Checkbutton(top, text='PYTHON1', variable=IntVar(), onvalue=1, offvalue=0, height=2, width=12)
checkbutton3.pack()

top.mainloop()
