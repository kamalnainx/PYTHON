# from tkinter import *

# top=Tk()

# top.geometry("200x200")

# frame=Frame(top)
# frame.pack()

# btn1=Button(frame, text="submit frame", fg="red", bg="pink", activebackground="red", activeforeground="pink")
# btn1.pack(side=LEFT)


# top.mainloop()



































# from tkinter import *

# top=Tk()

# top.geometry("200x200")

# frame=Frame(top)
# frame.pack()

# leftframe=Frame(top)
# leftframe.pack(side=LEFT)

# btn1=Button(frame, text="submit frame", fg="red", bg="pink", activebackground="red", activeforeground="pink")
# btn1.pack(side=LEFT)


# btn2=Button(leftframe, text="submit frame", fg="red", bg="pink", activebackground="red", activeforeground="pink")
# btn2.pack(side=RIGHT)


# top.mainloop()





























from tkinter import *

top=Tk()

top.geometry("200x200")

frame=Frame(top)
frame.pack()

leftframe=Frame(top)
leftframe.pack(side=LEFT)

rightframe=Frame(top)
rightframe.pack(side=LEFT)



btn1=Button(frame, text="btn1 frame", fg="red", bg="pink", activebackground="red", activeforeground="pink")
btn1.pack(side=LEFT)

btn2=Button(frame, text="btn2 frame", fg="red", bg="pink", activebackground="red", activeforeground="pink")
btn2.pack(side=RIGHT)

btn3=Button(rightframe, text="btn3 rightframe", fg="red", bg="pink", activebackground="red", activeforeground="pink")
btn3.pack(side=RIGHT)

btn4=Button(leftframe, text="btn4 leftframe", fg="red", bg="pink", activebackground="red", activeforeground="pink")
btn4.pack(side=RIGHT)

top.mainloop()

















