# from tkinter import *

# # import tkinter as tk


# top = Tk()

# top.geometry("300x300")

# radio=IntVar()



# msg = Message(top, text="radio").pack()

# r1=Radiobutton(top, text="Male", variable=radio, value=1)
# r1.pack(anchor=W)

# r2=Radiobutton(top, text="FeMale", variable=radio, value=2)
# r2.pack(anchor=W)

# r3=Radiobutton(top, text="Other", variable=radio, value=3)
# r3.pack(anchor=W)

# label=Label(top).pack()
# top.mainloop()























# from tkinter import *
# from tkinter.ttk import *

# top=Tk()

# top.geometry("300x300")

# style=Style(top)
# style.configure("TRadiobutton",background="green", forground="light green" , font=("arial", 10, "bold"))
# v=StringVar(top,"1")
# values={
#     "Male":"1",
#     "FeMale":"2",
#     "Other":"3",
    
# }


# for (text, value) in values.items():
#     Radiobutton(top,text=text, variable=v, value=value).pack(side=TOP, ipady=20 )
# top.mainloop()





























# from tkinter import *
# from tkinter.ttk import *

# top=Tk()

# top.geometry("300x300")

# style=Style(top)
# style.configure("TRadiobutton",background="green", forground="light green" , font=("arial", 10, "bold"))
# v=StringVar(top,"1")
# values={
#     "Male":"1",
#     "FeMale":"2",
#     "Other":"3",
    
# }

# y1=20
# for (text, value) in values.items():
#     Radiobutton(top,text=text, variable=v, value=value).place(x=20, y=y1)
#     y1=y1+40
# top.mainloop()
