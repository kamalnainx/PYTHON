from tkinter import *

top=Tk()

top.geometry("200x200")

def open():
    subtop=Toplevel(top)
    subtop.mainloop()

btn=Button(top, text="open 2nd from", command=open)
btn.place(x=70, y=80)

top.mainloop()





