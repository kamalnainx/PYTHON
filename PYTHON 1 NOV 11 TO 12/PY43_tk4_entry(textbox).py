##from tkinter import *
##
##top=Tk()
##
##top.geometry("500x400")
##
##name1=Label(top,text="what is your name").place(x=25,y=50)
##name1=Entry(top).place(x=125,y=50)
##top.mainloop()








##
##from tkinter import *
##
##top=Tk()
##top.geometry("300x300")
##
##luserinfo1=Label(top,text="Enter user informetion").place(x=100,y=25)
##
##lname1=Label(top,text="what is your name").place(x=25,y=50)
##ename1=Entry(top).place(x=150,y=50)
##
##age1=Label(top,text="what is your age").place(x=25,y=75)
##eage1=Entry(top).place(x=150,y=75)
##
##email1=Label(top,text="what is your email").place(x=25,y=100)
##eemail1=Entry(top).place(x=150,y=100)
##
##password1=Label(top,text="what is your password").place(x=25,y=125)
##epassword1=Entry(top).place(x=150,y=125)
##
##top.mainloop()












##from tkinter import *
##
##top=Tk()
##top.geometry("300x250")
##
##luserinfo1=Label(top,text="Enter user informetion").place(x=100,y=25)
##
##lname1=Label(top,text="what is your name").place(x=25,y=50)
##ename1=Entry(top).place(x=150,y=50)
##
##age1=Label(top,text="what is your age").place(x=25,y=75)
##eage1=Entry(top).place(x=150,y=75)
##
##email1=Label(top,text="what is your email").place(x=25,y=100)
##eemail1=Entry(top).place(x=150,y=100)
##
##password1=Label(top,text="what is your password").place(x=25,y=125)
##epassword1=Entry(top).place(x=150,y=125)
##
##
##sbutton1=Button(top,text="submit this data",activebackground="pink",activeforeground="green").place(x=150,y=175)
##top.mainloop()










##from functools import partial
##import tkinter as tk
##
##def add1(label_result,n1,n2):
##    num1=(n1.get())
##    num2=(n2.get())
##    result=int(num1)+int(num2)
##    label_result.config(text="final total is= %d" % result)
##    return
##
##top=tk.Tk()
##top.geometry("300x250+100+200")
##
##luserinfo1=tk.Label(top,text="add two number").place(x=100,y=25)#title
##
##lnum1=tk.Label(top,text="enter 1st number").place(x=25,y=50)#num1
##number1=tk.StringVar()
##enum1=tk.Entry(top, textvariable=number1).place(x=150,y=50)
##
##lnum2=tk.Label(top,text="enter 2 number").place(x=25,y=75)#num2
##number2=tk.StringVar()
##enum2=tk.Entry(top, textvariable=number2).place(x=150,y=75)
##
##
##lableResult=tk.Label(top).place(x=150,y=100)
##
##add1=partial(add1,lableResult,number1,number2)
##
##
##totalbutton1=tk.Button(top,text="add",activebackground="pink",activeforeground="green",command=add1).place(x=150,y=175)
##
##
##top.mainloop()










##import tkinter as tk
##from functools import partial
##
##def call_result(label_result, n1, n2):
##    num1=(n1.get())
##    num2=(n2.get())
##    result=int(num1)+int(num2)
##    label_result.config(text="Result=%d" % result)
##    return
##
##root=tk.Tk()
##root.geometry('400x200+100+200')
##
##number1=tk.StringVar()
##number2=tk.StringVar()
##
##
##
##root.title("add 2 number")
##
##
##labelnum1=tk.Label(root,text='num1').grid(row=1,column=0)
##labelnum2=tk.Label(root,text='num2').grid(row=2,column=0)
##
##entrynum1=tk.Entry(root,textvariable=number1).grid(row=1,column=2)
##entrynum2=tk.Entry(root,textvariable=number2).grid(row=2,column=2)
##
##lableresult=tk.Label(root)
##lableresult.grid(row=5,column=2)
##
##call_result=partial(call_result,lableresult, number1, number2)
##
##buttoncall=tk.Button(root,text="+",command=call_result).grid(row=3, column=1)
##root.mainloop()




















from tkinter import *

root=Tk()
root.geometry('400x200')

number1=StringVar()
number2=StringVar()



root.title("login from")


labelnum1=Label(root,text='user id').grid(row=1,column=1)
labelnum2=Label(root,text='user password').grid(row=3,column=1)

entrynum1=Entry(root,textvariable=number1).grid(row=1,column=3)
entrynum2=Entry(root,textvariable=number2).grid(row=3,column=3)

buttoncall=Button(root,text="login").grid(row=5, column=2)
root.mainloop()
