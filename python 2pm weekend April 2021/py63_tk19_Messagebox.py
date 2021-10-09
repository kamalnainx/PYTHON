# from tkinter import *

# from tkinter import messagebox

# top = Tk()
# top.geometry("1x1")

# messagebox.showinfo("informatio","Information")
# # top.mainloop()








































# from tkinter import *

# from tkinter import messagebox

# top = Tk()
# top.geometry("1x1")

# messagebox.showwarning("warning","Warning")
# # top.mainloop()









































# from tkinter import *

# from tkinter import messagebox

# top = Tk()
# top.geometry("1x1")

# messagebox.showerror("error","Error")
# # top.mainloop()









































# from tkinter import *

# from tkinter import messagebox

# top = Tk()
# top.geometry("1x1")

# messagebox.askquestion("Final","Do you want to exit.")
# top.mainloop()









































# from tkinter import *

# from tkinter import messagebox

# top = Tk()
# top.geometry("1x1")

# messagebox.askokcancel("Final","Do you want to exit.")
# top.mainloop()









































# from tkinter import *

# from tkinter import messagebox

# top = Tk()
# top.geometry("1x1")

# messagebox.askyesno("Application","Do you want to exit.")
# # top.mainloop()









































# from tkinter import *

# from tkinter import messagebox

# top = Tk()
# top.geometry("1x1")

# messagebox.askretrycancel("Application","try it again?")
# # top.mainloop()









































# from tkinter import *

# from tkinter import messagebox

# top = Tk()
# top.geometry("1x1")

# messagebox.askyesnocancel("Application","Do you want to save or not.")
# # top.mainloop()









































# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox as mb

# def fun1():
#     res=mb.askquestion("Exit?","do you want to exit from application.")

#     if res=="yes":
#         top.destroy()
#     else:
#         mb.showinfo("Return", "returing to main application.")
# top=tk.Tk()

# canvas = tk.Canvas(top, width="200", height="200")

# canvas.pack()
# b1=Button(top, text="Quit Application", command=fun1)

# canvas.create_window(100, 100, window=b1)
# top.mainloop()































# import tkinter as tk
# from functools import partial
# from tkinter import *
# from tkinter import messagebox as mb

# def fun1():
#     res=mb.askquestion("Exit?","do you want to exit from application.")

#     if res=="yes":
#         top.destroy()
#     else:
#         mb.showinfo("Return", "returing to main application.")

# top=tk.Tk()

# canvas = tk.Canvas(top, width="400", height="400")

# canvas.pack()
# b1=Button(top, text="Quit Application", command=fun1)

# canvas.create_window(300, 300, window=b1)





# def call_result(lable_result, n1,n2):
#     num1=(n1.get())
#     num2=(n2.get())
#     result=int(num1)+int(num2)
#     lable_result.config(text="result = %d" % result)
#     return

# def call_zero(lable_result,n1,n2):
#     # num1= " "
#     # num2=" "
#     entrynum1=tk.Entry(top, textvariable="")
#     entrynum2=tk.Entry(top, textvariable="")
#     entrynum1.place(x=80, y=40)
#     entrynum2.place(x=80, y=80)

#     lable_result.config(text=" " )
#     return


# labelNum1=tk.Label(top, text=" num1 ")
# labelNum2=tk.Label(top, text=" num2 ")

# labelNum1.place(x=30, y=40)
# labelNum2.place(x=30, y=80)

# number1=tk.StringVar()
# number2=tk.StringVar()

# entrynum1=tk.Entry(top, textvariable=number1)
# entrynum2=tk.Entry(top, textvariable=number2)


# entrynum1.place(x=80, y=40)
# entrynum2.place(x=80, y=80)

# labelResult=tk.Label(top)
# labelResult.place(x=80, y=160)


# total1=partial(call_result,labelResult,number1,number2)

# reset1=partial(call_zero,labelResult,number1,number2)

# b1=tk.Button(top, text="total", command=total1)
# b1.place(x=80, y=120)

# b2=tk.Button(top, text="reset", command=reset1)
# b2.place(x=120, y=120)

# top.mainloop()























# from tkinter import *
 
# def delete():
#     myentry.delete(3, 'end')
 
# root = Tk()
# root.geometry('180x120')
 
# myentry = Entry(root, width = 20)
# myentry.pack(pady = 5)
 
# mybutton = Button(root, text = "Delete", command = delete)
# mybutton.pack(pady = 5)
 
# root.mainloop()



































import tkinter as tk
from functools import partial
from tkinter import *
from tkinter import messagebox as mb

def fun1():
    res=mb.askquestion("Exit?","do you want to exit from application.")

    if res=="yes":
        top.destroy()
    else:
        mb.showinfo("Return", "returing to main application.")

top=tk.Tk()

canvas = tk.Canvas(top, width="400", height="400")

canvas.pack()
b1=Button(top, text="Quit Application", command=fun1)

canvas.create_window(300, 300, window=b1)





def call_result(lable_result, n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result=int(num1)+int(num2)
    lable_result.config(text="result = %d" % result)
    return



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


def delete(lable_result):
    entrynum1.delete( 0, 'end')
    entrynum2.delete( 0, 'end')
    lable_result.config(text=" " )
    return

del1=partial(delete,labelResult)

b1=tk.Button(top, text="total", command=total1)
b1.place(x=80, y=120)

b2=tk.Button(top, text="reset", command=del1)
b2.place(x=120, y=120)

top.mainloop()





