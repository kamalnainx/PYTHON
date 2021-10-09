from tkinter import *

top=Tk()

top.geometry("400x400")

uname =Label(top,text="User Name")
uname.place(x=20, y=40)

Password =Label(top,text="Password")
Password.place(x=20, y=80)

e1=Entry(top, width=20)
e1.place(x=100, y=40)

e2=Entry(top, width=20)
e2.place(x=100, y=80)


btn1=Button(top, text="login", fg="red", bg="pink", activebackground="red", activeforeground="pink")
btn1.place(x=100, y=120)


top.mainloop()















