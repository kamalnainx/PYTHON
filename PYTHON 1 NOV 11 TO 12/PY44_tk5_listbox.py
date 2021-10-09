##
##from tkinter import *
##
##root=Tk()
##root.geometry('200x200')
##
##root.title("list box")
##
##label1=Label(root,text="this is list of topics").grid(row=2,column=1)
##
##listbox1=Listbox(root)
##
##listbox1.insert(1,"c")
##listbox1.insert(2,"c++")
##listbox1.insert(3,"JAVA")
##listbox1.insert(4,"PYTHON")
##listbox1.insert(5,"POWER BI")
##
##listbox1.grid(row=4,column=1)
##
##root.mainloop()














from tkinter import *

root=Tk()
root.geometry('200x200')

root.title("list box")

label1=Label(root,text="this is list of topics").grid(row=2,column=1)

listbox1=Listbox(root)

listbox1.insert(1,"c")
listbox1.insert(2,"c++")
listbox1.insert(3,"JAVA")
listbox1.insert(4,"PYTHON")
listbox1.insert(5,"POWER BI")

listbox1.grid(row=4,column=1)

button1=Button(root,text="delete",command=lambda listbox1=listbox1: listbox1.delete(ANCHOR)).grid(row=3,column=1)
root.mainloop()
