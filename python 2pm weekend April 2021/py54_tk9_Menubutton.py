from tkinter import *

top=Tk()

top.geometry("400x400")

uname =Label(top,text="color menu")
uname.place(x=20, y=40)


mb1=Menubutton(top,text="color", relief=FLAT)

mb1.menu=Menu(mb1)

mb1["menu"]=mb1.menu

mb1.menu.add_checkbutton(label="red", variable=IntVar() )
mb1.menu.add_checkbutton(label="Green")
mb1.menu.add_checkbutton(label="Blue")
mb1.menu.add_checkbutton(label="Yellow")
mb1.menu.add_checkbutton(label="Pink")

mb1.place(x=100, y=40)



btn1=Button(top, text="login", fg="red", bg="pink", activebackground="red", activeforeground="pink")
btn1.place(x=100, y=220)


top.mainloop()


