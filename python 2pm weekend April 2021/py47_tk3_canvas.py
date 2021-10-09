# from tkinter import *

# top =Tk()

# c=Canvas(top).pack()

# top.mainloop()










































# from tkinter import *

# top =Tk()

# top.geometry("600x600")


# c=Canvas(top,bg="pink")
# c.pack()

# top.mainloop()







































# from tkinter import *

# top =Tk()

# top.geometry("400x400")


# c=Canvas(top,   bg="pink",  height="200")
# c.pack()

# top.mainloop()







































from tkinter import *

top =Tk()

top.geometry("400x400")


c=Canvas(top,   bg="pink",  height="200")

arc=c.create_arc((5,10,150,200),start=0, extent=150, fill="red")

c.pack()

top.mainloop()




























