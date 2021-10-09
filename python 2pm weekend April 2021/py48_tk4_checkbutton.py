# from tkinter import *

# top=Tk()

# top.geometry("300x300")

# cb1=Checkbutton(top, text="red", onvalue=1, offvalue=0, height=2, width=10).pack()



# top.mainloop()






































# from tkinter import *

# top=Tk()

# top.geometry("300x300")

# cb1=Checkbutton(top, text="red", onvalue=1, offvalue=0, height=2, width=10).pack()

# cb2=Checkbutton(top, text="green", onvalue=1, offvalue=0, height=2, width=10).pack()

# cb3=Checkbutton(top, text="blue", onvalue=1, offvalue=0, height=2, width=10).pack()



# top.mainloop()



































from tkinter import *

top=Tk()

top.geometry("300x300")

cb1=Checkbutton(top, text="red", variable=IntVar, onvalue=1, offvalue=0, height=2, width=10).pack()

cb2=Checkbutton(top, text="green", variable=IntVar, onvalue=1, offvalue=0, height=2, width=10).pack()

cb3=Checkbutton(top, text="blue", variable=IntVar, onvalue=1, offvalue=0, height=2, width=10).pack()



top.mainloop()



