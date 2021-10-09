# from tkinter import *

# top=Tk()

# top.geometry("400x400")

# uname =Label(top,text="ListBox")
# uname.place(x=20, y=40)


# lb1=Listbox(top)

# lb1.insert(1,"red")
# lb1.insert(2,"Green")
# lb1.insert(3,"Blue")
# lb1.insert(4,"Yellow")
# lb1.insert(5,"Pink")

# lb1.place(x=100, y=40)



# btn1=Button(top, text="login", fg="red", bg="pink", activebackground="red", activeforeground="pink")
# btn1.place(x=100, y=220)


# top.mainloop()






















from tkinter import *

top=Tk()

top.geometry("400x400")

uname =Label(top,text="ListBox")
uname.place(x=20, y=40)


lb1=Listbox(top)

lb1.insert(1,"red")
lb1.insert(2,"Green")
lb1.insert(3,"Blue")
lb1.insert(4,"Yellow")
lb1.insert(5,"Pink")

lb1.place(x=100, y=40)


btn1=Button(top, text="remove", fg="red", bg="pink", activebackground="red", activeforeground="pink", command= lambda lb1=lb1:lb1.delete(ANCHOR))
btn1.place(x=100, y=220)


top.mainloop()

