# from tkinter import *

# top = Tk()

# top.geometry("400x400")

# name = Label(top,text="Name")

# email = Label(top,text="Email Id")

# password = Label(top,text="Password")


# name.place(x=20, y=40)

# email.place(x=20, y=80)

# password.place(x=20, y=120)



# top.mainloop()



























# from tkinter import *

# top = Tk()

# top.geometry("400x400")

# name = Label(top,text="Name")

# email = Label(top,text="Email Id")

# password = Label(top,text="Password")


# name.place(x=20, y=40)

# email.place(x=20, y=80)

# password.place(x=20, y=120)


# tb1=Entry(top)

# tb2=Entry(top)

# tb3=Entry(top)


# tb1.place(x=80,y=40)

# tb2.place(x=80,y=80)

# tb3.place(x=80,y=120)


# top.mainloop()















# from tkinter import *

# top = Tk()

# top.geometry("400x400")

# name = Label(top,text="Name")

# email = Label(top,text="Email Id")

# password = Label(top,text="Password")


# name.place(x=20, y=40)

# email.place(x=20, y=80)

# password.place(x=20, y=120)


# tb1=Entry(top)

# tb2=Entry(top)

# tb3=Entry(top)


# tb1.place(x=80,y=40)

# tb2.place(x=80,y=80)

# tb3.place(x=80,y=120)


# b1=Button(top, text="Submit")

# b1.place(x=80, y=160)

# top.mainloop()





























































import tkinter as tk
from functools import partial

def call_result(lable_result, n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result=int(num1)+int(num2)
    lable_result.config(text="result = %d" % result)
    return

top= tk.Tk()
top.geometry("400x400")

labelNum1=tk.Label(top, text=" num1 ")
labelNum2=tk.Label(top, text=" num2 ")

labelNum1.place(x=30, y=40)
labelNum2.place(x=30, y=80)

number1=tk.StringVar()
number2=tk.StringVar()

entrynum1=tk.Entry(top, textvariable=number1)
entrynum2=tk.Entry(top, textvariable=number2)


entrynum1.place(x=80, y=40)
entrynum2.place(x=80, y=80)

labelResult=tk.Label(top)
labelResult.place(x=80, y=160)


total1=partial(call_result,labelResult,number1,number2)

b1=tk.Button(top, text="total", command=total1)
b1.place(x=80, y=120)

top.mainloop()
