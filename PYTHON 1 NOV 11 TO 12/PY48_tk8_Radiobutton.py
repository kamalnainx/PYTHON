from tkinter import *
top=Tk()
top.geometry("300x200")
def selection():
    selection="your selected radio button"+str(radio1.get())
    labelselection1.config(text=selection)

radio1=IntVar()
label1=Label(text="select any one from this option")
label1.pack()

radiobutton1=Radiobutton(top,text="Excel",variable=radio1,value=1,command=selection)
radiobutton1.pack(anchor=W)
radiobutton2=Radiobutton(top,text="POWER BI",variable=radio1,value=2,command=selection)
radiobutton2.pack(anchor=W)
radiobutton3=Radiobutton(top,text="SQL SERVER",variable=radio1,value=3,command=selection)
radiobutton3.pack(anchor=W)

labelselection1=Label(top)
labelselection1.pack()
top.mainloop()
