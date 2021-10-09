##from tkinter import *
##
##root=Tk()
##root.geometry('200x200')
##
##root.title("Menu Button")
##
##menubutton1=Menubutton(root,text="file",relief=FLAT)
##menubutton1.grid()
##menubutton1.menu=Menu(menubutton1)
##menubutton1["menu"]=menubutton1.menu
##menubutton1.menu.add_checkbutton(label="save", variable=IntVar())
##menubutton1.pack()
##root.mainloop()







from tkinter import *

root=Tk()
root.geometry('200x200')

root.title("Menu Button")

menubutton1=Menubutton(root,text="file",relief=FLAT)
menubutton1.grid()
menubutton1.menu=Menu(menubutton1)
menubutton1["menu"]=menubutton1.menu
menubutton1.menu.add_checkbutton(label="save", variable=IntVar())
menubutton1.menu.add_checkbutton(label="open", variable=IntVar())
menubutton1.menu.add_checkbutton(label="exit", variable=IntVar())
menubutton1.pack()
root.mainloop()
