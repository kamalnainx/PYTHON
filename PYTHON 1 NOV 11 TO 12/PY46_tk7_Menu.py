##from tkinter import *
##
##root=Tk()
##
##root.geometry('200x200')
##
##root.title("Menu Bar")
##def file1():
##        print("this is file menu")
##
##menubar1=Menu(root)
##
##menubar1.add_command(label="File", command=file1)
##menubar1.add_command(label="edit", command=root.quit)
##
##
##root.config(menu=menubar1)
##root.mainloop()







##
##from tkinter import *
##
##root=Tk()
##
##root.geometry('200x200')
##
##root.title("Menu Bar")
##menubar1=Menu(root)
##
##file1=Menu(menubar1,tearoff=0)
##file1.add_command(label="New")
##file1.add_command(label="OPEN")
##file1.add_command(label="SAVE")
##file1.add_command(label="SAVE AS")
##file1.add_command(label="PRINT")
##file1.add_command(label="EXIT")
##
##menubar1.add_cascade(label="FILE",menu=file1)
##
##
##root.config(menu=menubar1)
##root.mainloop()















##from tkinter import *
##
##root=Tk()
##
##root.geometry('200x200')
##
##root.title("Menu Bar")
##menubar1=Menu(root)
##
##file1=Menu(menubar1,tearoff=0)
##file1.add_command(label="New")
##file1.add_command(label="OPEN")
##file1.add_command(label="SAVE")
##file1.add_command(label="SAVE AS")
##file1.add_command(label="PRINT")
##file1.add_separator()
##file1.add_command(label="EXIT")
##
##menubar1.add_cascade(label="FILE",menu=file1)
##
##
##root.config(menu=menubar1)
##root.mainloop()














##from tkinter import *
##
##root=Tk()
##
##root.geometry('200x300')
##
##root.title("Menu Bar")
##menubar1=Menu(root)
##
##file1=Menu(menubar1,tearoff=0)
##file1.add_command(label="New")
##file1.add_command(label="OPEN")
##file1.add_command(label="SAVE")
##file1.add_command(label="SAVE AS")
##file1.add_command(label="PRINT")
##file1.add_separator()
##file1.add_command(label="EXIT")
##
##menubar1.add_cascade(label="FILE",menu=file1)
##
##
##edit1=Menu(menubar1,tearoff=0)
##edit1.add_command(label="UNDO")
##edit1.add_command(label="REDO")
##edit1.add_separator()
##edit1.add_command(label="CUT")
##edit1.add_command(label="COPY")
##edit1.add_command(label="PASTE")
##edit1.add_command(label="DEL")
##edit1.add_command(label="ALL SELECT")
##edit1.add_separator()
##edit1.add_command(label="FIND")
##edit1.add_command(label="REPLACE")
##edit1.add_command(label="GO TO")
##
##
##menubar1.add_cascade(label="EDIT",menu=edit1)
##
##
##root.config(menu=menubar1)
##root.mainloop()












from tkinter import *

root=Tk()

root.geometry('300x300')

root.title("Menu Bar")
menubar1=Menu(root)

file1=Menu(menubar1,tearoff=0)
file1.add_command(label="New")
file1.add_command(label="OPEN")
file1.add_command(label="SAVE")
file1.add_command(label="SAVE AS")
file1.add_command(label="PRINT")
file1.add_separator()
file1.add_command(label="EXIT")
menubar1.add_cascade(label="FILE",menu=file1)


edit1=Menu(menubar1,tearoff=0)
edit1.add_command(label="UNDO")
edit1.add_command(label="REDO")
edit1.add_separator()
edit1.add_command(label="CUT")
edit1.add_command(label="COPY")
edit1.add_command(label="PASTE")
edit1.add_command(label="DEL")
edit1.add_command(label="ALL SELECT")
edit1.add_separator()
edit1.add_command(label="FIND")
edit1.add_command(label="REPLACE")
edit1.add_command(label="GO TO")
menubar1.add_cascade(label="EDIT",menu=edit1)

help1=Menu(menubar1,tearoff=0)
help1.add_command(label="HELP")
help1.add_command(label="ABOUT APP")
edit1.add_separator()
menubar1.add_cascade(label="HELP",menu=help1)

root.config(menu=menubar1)
root.mainloop()
