##from tkinter import*
##top =Tk()
##top.geometry("300x300")
##
##labelframe1=LabelFrame(top, text="Positive commentas")
##labelframe1.pack(fill="both",expand="yes")
##
##toplabel=Label(labelframe1, text="place to put the Positive comments")
##toplabel.pack()
##
##top.mainloop()







from tkinter import*
top =Tk()
top.geometry("300x300")

labelframe1=LabelFrame(top, text="Positive commentas")
labelframe1.pack(fill="both",expand="yes")

toplabel=Label(labelframe1, text="place to put the Positive comments")
toplabel.pack()

labelframe2=LabelFrame(top, text="Negative commentas")
labelframe2.pack(fill="both",expand="yes")

bottomlabel=Label(labelframe2, text="place to put the Negative comments")
bottomlabel.pack()

top.mainloop()
