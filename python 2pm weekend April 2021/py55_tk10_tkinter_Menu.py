# from tkinter import *

# Top = Tk()

# menubar=Menu(Top)

# menubar.add_command(label="File")

# Top.config(menu=menubar)

# Top.mainloop()






































# from tkinter import *

# Top = Tk()

# menubar=Menu(Top)

# menubar.add_command(label="File")
# menubar.add_command(label="Edit")
# menubar.add_command(label="Selection")

# Top.config(menu=menubar)

# Top.mainloop()





































# from tkinter import *

# Top = Tk()

# def f1():
#     print("this is file menu")

# menubar=Menu(Top)

# menubar.add_command(label="File", command=f1)
# menubar.add_command(label="Edit")
# menubar.add_command(label="Selection")

# Top.config(menu=menubar)

# Top.mainloop()


































# from tkinter import *

# Top = Tk()


# menubar=Menu(Top)

# # file menu
# file=Menu(menubar, tearoff=0)

# file.add_command(label="New")
# file.add_command(label="Open")
# file.add_command(label="Save")
# file.add_command(label="Save as")
# file.add_command(label="Exit")

# menubar.add_cascade(label="File", menu=file)

# menubar.add_command(label="Edit")
# menubar.add_command(label="Selection")



# Top.config(menu=menubar)

# Top.mainloop()
























# from tkinter import *

# Top = Tk()

# menubar=Menu(Top)

# # file menu
# file=Menu(menubar, tearoff=0)

# file.add_command(label="New")
# file.add_command(label="Open")
# file.add_command(label="Save")
# file.add_command(label="Save as")
# file.add_command(label="Print")

# file.add_separator()
# file.add_command(label="Exit")

# menubar.add_cascade(label="File", menu=file)



# menubar.add_command(label="Edit")
# menubar.add_command(label="Selection")



# Top.config(menu=menubar)

# Top.mainloop()




















from tkinter import *

Top = Tk()

menubar=Menu(Top)

# file menu
file=Menu(menubar, tearoff=0)

file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as")
file.add_command(label="Print")

file.add_separator()
file.add_command(label="Exit")

menubar.add_cascade(label="File", menu=file)


# edit menu
edit=Menu(menubar, tearoff=0)

edit.add_command(label="Undo")
edit.add_command(label="Redo")

edit.add_separator()

edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")

edit.add_separator()
edit.add_command(label="select all")

menubar.add_cascade(label="Edit", menu=edit)



# view menu
view=Menu(menubar, tearoff=0)

view.add_command(label="Next")
view.add_command(label="Pre")

view.add_separator()

view.add_command(label="Help")

menubar.add_cascade(label="view", menu=view)



Top.config(menu=menubar)

Top.mainloop()
