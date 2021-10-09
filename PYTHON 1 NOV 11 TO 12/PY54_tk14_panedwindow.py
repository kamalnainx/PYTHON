from tkinter import *

def add():
    a=int(e1.get())
    b=int(e1.get)()
    leftdata=str(a+b)
    left.insert(1,leftdata)

w1=PanedWindow()
w1.pack(fill=BOTH,expand=1)


left1=Entry(w1,bd=5)
w1.add(left1)

w2=PanedWindow(w1,orient =VERTICAL)
w1.add(w2)

e1=Entry(w2)
e2=Entry(w2)

w2.add(e1)
w2.add(e2)

button1=Button(w2,text="add",command="and")
w2.add(button1)
mainloop()



       
