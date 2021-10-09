from tkinter import *

root=Tk()

root.geometry("300x200")

spin.Spinbox(root,from_=0 ,to=25)

spin.pack()


root.mainloop()


##from tkinter import *
##
##root=Tk()
##
##root.geometry("300x200")
##
##def open():
##    top1=Toplevel(root)
##    top1.mainloop()
##
##button1=Button(root,text="open top level", command=open)
##button1.place(x=100,y=100)
##
##root.mainloop()
