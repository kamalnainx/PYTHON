from tkinter import *

top=Tk()

top.geometry("300x200")

sb=Scrollbar(top)
sb.pack(side=RIGHT,fill=Y)
mylist=Listbox(top,yscrollcommand=sb.set)
for line in range(30):
    M=mylist.insert(END,"Day Number"+str(line))
mylist.pack(side=LEFT)
sb.config(command=mylist.yview)
top.mainloop()
