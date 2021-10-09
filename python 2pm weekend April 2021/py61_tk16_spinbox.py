from tkinter import *

top=Tk()

top.geometry("200x200")

spin = Spinbox(top, from_=0, to=30)
spin.place(x=30, y=50)

btn=Button(top, text="open 2nd from")
btn.place(x=60, y=100)

top.mainloop()





