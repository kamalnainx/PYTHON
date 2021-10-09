##from tkinter import *
##top=Tk()#app window
##b1=Button(top, text="button1")
##b1.pack(side=TOP)
##top.mainloop()#main loop=event=Entering in from







##from tkinter import *
##top=Tk()#app window
##b1=Button(top, text="button1",fg='red')
##b1.pack(side=TOP)
##top.mainloop()#main loop=event=Entering in from







##from tkinter import *
##top=Tk()#app window
##b1=Button(top, text="button1",fg='red')
##b1.pack(side=TOP)
##b2=Button(top, text="button2",fg='green')
##b2.pack(side=BOTTOM)
##top.mainloop()#main loop=event=Entering in from






##from tkinter import *
##top=Tk()#app window
##b1=Button(top, text="button1",fg='red')
##b1.pack(side=TOP)
##b2=Button(top, text="button2",fg='green')
##b2.pack(side=RIGHT)
##b1=Button(top, text="button3",fg='blue')
##b1.pack(side=BOTTOM)
##b2=Button(top, text="button4",fg='yellow')
##b2.pack(side=LEFT)
##top.mainloop()#main loop=event=Entering in from










##from tkinter import *
##top=Tk()#app window
##top.geometry('300x300')
##b1=Button(top, text="button1",fg='red')
##b1.pack(side=TOP)
##b2=Button(top, text="button2",fg='green')
##b2.pack(side=RIGHT)
##b1=Button(top, text="button3",fg='blue')
##b1.pack(side=BOTTOM)
##b2=Button(top, text="button4",fg='yellow')
##b2.pack(side=LEFT)
##top.mainloop()#main loop=event=Entering in from









from tkinter import *
import tkMessageBox

top=Tk()#app window
top.geometry('300x300')

def fun():
    tkMessageBox.showinfo("hello", "this is red button")

b1=Button(top, text="red button1",activeforeground="red", command=fun, activebacjground='pink',pady=10)
b1.pack(side=TOP)
b2=Button(top, text="button2",activeforeground='green', command=fun, activebacjground='pink',pady=10)
b2.pack(side=RIGHT)
b1=Button(top, text="button3",activeforeground='blue', command=fun, activebacjground='pink',pady=10)
b1.pack(side=BOTTOM)
b2=Button(top, text="button4",activeforeground='blue', command=fun, activebacjground='pink',pady=10)
b2.pack(side=LEFT)
top.mainloop()#main loop=event=Entering in from
