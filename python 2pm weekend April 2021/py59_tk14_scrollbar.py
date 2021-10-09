# from tkinter import *

# top=Tk()


# sb=Scrollbar(top)
# sb.pack(side=RIGHT, fill=Y)

# top.mainloop()








































# from tkinter import *

# top=Tk()

# top.geometry("100x100")

# sb=Scrollbar(top)
# sb.pack(side=BOTTOM, fill=X)


# top.mainloop()







































# from tkinter import *

# top=Tk()

# top.geometry("100x100")

# sb=Scrollbar(top)
# sb.pack(side=RIGHT, fill=Y)

# mylist1=Listbox(top, yscrollcommand=sb.set)

# mylist1.insert(END,"item 1")

# mylist1.pack(side=LEFT)

# top.mainloop()


































# from tkinter import *

# top=Tk()

# top.geometry("100x100")

# sb=Scrollbar(top)
# sb.pack(side=RIGHT, fill=Y)

# mylist1=Listbox(top, yscrollcommand=sb.set)

# mylist1.insert(END,"item 1")
# mylist1.insert(END,"item 2")
# mylist1.insert(END,"item 3")

# mylist1.pack(side=LEFT)

# top.mainloop()
































from tkinter import *

top=Tk()

top.geometry("100x100")

sb=Scrollbar(top)
sb.pack(side=RIGHT, fill=Y)

mylist1=Listbox(top, yscrollcommand=sb.set)

for i in range(50):
    mylist1.insert(END,"item "+str(i))

mylist1.pack(side=LEFT)

sb.config(command=mylist1.yview)

top.mainloop()
