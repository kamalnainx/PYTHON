# class my_class1:
#     pass







# class Myclass1:
#     x=10
# print(Myclass1)    

















# class Myclass1:
#     x=10

# obj1=Myclass1()
# print(obj1)    















# class Myclass1:
#     x=10

# print(Myclass1().x)














































# class Myclass1:
#     x=10

# obj1=Myclass1()
# print(obj1.x)













































# def myfun1(apple):
#     print("my function"+apple)
# myfun1("A Big Apple")















































# class Myclass1:
#     x=10
#     def myfun1(self):
#         print("this is my first function inside of class")

# obj1=Myclass1()
# print(obj1.x)
# obj1.myfun1()










































# class Myclass1:
#     x=10
#     def myfun1(self, uname):
#         print("The user name is "+uname)

# obj1=Myclass1()
# print(obj1.x)
# obj1.myfun1("kamal nain")










































# class Myclass1:
#     def __init__(self) -> None:
#         pass
#     x=10
#     def myfun1(self, uname):
#         print("The user name is "+uname)

# obj1=Myclass1()
# print(obj1.x)
# obj1.myfun1("kamal nain")








































# class Myclass1:
#     def __init__(self):
#         print("this is class method")
#     x=10
#     def myfun1(self, uname):
#         print("The user name is "+uname)

# obj1=Myclass1()
# print(obj1.x)
# obj1.myfun1("kamal nain")








































# class Myclass1:
#     def __init__(self,fname):
#         print("user name:- "+fname)
#         self.x=fname
#     def x1(self):
#         print("the x is ",self.x)
#     def myfun1(self, uname):
#         print("The user name is "+uname)

# obj1=Myclass1("kamal")
# print("x is:- ",obj1.x)
# obj1.myfun1("kamal nain")
# obj1.x1()





































# class Myclass1:
#     def __init__(self,fname):
#         print("user name:- "+fname)
#         self.x=fname
#     def myfun1(self, uname):
#         print("The user name is "+uname+" "+self.x)

# obj1=Myclass1("kamal")
# print("x is:- ",obj1.x)
# obj1.myfun1("kamal nain")








































# class Myclass1:
#     def __init__(self,fname,lname) -> None:
#         self.fn=fname
#         self.ln=lname
#     def myfun1(self):
#         print("the user name is:- "+ self.fn+ " "   + self.ln)
# obj1=Myclass1("kamal","Nain")
# obj1.myfun1()

            








































# class Myclass1:
#     def __init__(self,fname,lname) -> None:
#         self.fn=fname
#         self.ln=lname
#     def myfun1(self):
#         print("the user name is:- "+ self.fn+ " "   + self.ln)
# obj1=Myclass1("kamal","Nain")
# obj1.fn="The Kamal"
# obj1.myfun1()









































# class Myclass1:
#     def __init__(self,fname,lname) -> None:
#         self.fn=fname
#         self.ln=lname
#     def myfun1(self):
#         print("the user name is:- "+ self.fn+ " "   + self.ln)
# obj1=Myclass1("kamal","Nain")
# obj1.fn="The Kamal"
# obj1.myfun1()
# print(obj1.fn)
# print(obj1.ln)







































# class Myclass1:
#     def __init__(self,fname,lname) -> None:
#         self.fn=fname
#         self.ln=lname
#     def myfun1(ms):
#         print("the user name is:- "+ ms.fn+ " "   + ms.ln)
# obj1=Myclass1("kamal","Nain")
# obj1.fn="The Kamal"
# obj1.myfun1()
# print(obj1.fn)
# print(obj1.ln)







































# class Myclass1:
#     def __init__(self,fname,lname):
#         self.fn=fname
#         self.ln=lname
#     def myfun1(ms):
#         print("the user name is:- "+ ms.fn+ " "   + ms.ln)
# obj1=Myclass1("kamal","Nain")
# obj1.fn="The Kamal"
# obj1.myfun1()

# print(obj1.fn)
# del obj1.ln
# print(obj1.ln)





































# class Myclass1:
#     def __init__(self,fname,lname):
#         self.fn=fname
#         self.ln=lname
#     def myfun1(ms):
#         print("the user name is:- "+ ms.fn+ " "   + ms.ln)
# obj1=Myclass1("kamal","Nain")
# obj1.fn="The Kamal"
# obj1.myfun1()
# del obj1
# print(obj1.fn)
# del obj1.ln
# print(obj1.ln)





def myfun1():
    print("function")

i=15
if i>10:
    myfun1()
else:
    print("i is small")