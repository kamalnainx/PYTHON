from tkinter import *

top=Tk()

top.geometry("300x200")

text=Text(top)
text.insert(INSERT,"Name....")
text.insert(END,"salary....")

text.pack()

text.tag_add("write here","1.0","1.4")
text.tag_add("chick here","1.8","1.13")

text.tag_config("write Here", background="yellow", foreground="black")
text.tag_config("click Here", background="black", foreground="yellow")


top.mainloop()
