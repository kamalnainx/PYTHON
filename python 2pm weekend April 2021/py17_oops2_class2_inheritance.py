# class Myclass1:
#     def __init__(self,name,age) :
#         self.uname1=name
#         self.uage1=age
#     def printuv(self):
#         print("user name is ",self.uname1,"\nuser age is ",self.uage1,)

# mc1=Myclass1("kamal",30)
# mc1.printuv()















# class Myclass1:
#     def __init__(self,name,age) :
#         self.uname1=name
#         self.uage1=age
#     def printuv(self):
#         print("user name is ",self.uname1,"\nuser age is ",self.uage1,)
        
# class Myclass2(Myclass1):
#     pass

# mc2=Myclass2("kamal",30)
# mc2.printuv()























# class Myclass1:
#     def __init__(self,name,age) :
#         self.uname1=name
#         self.uage1=age
#     def printuv(self):
#         print("user name is ",self.uname1,"\nuser age is ",self.uage1,)
        
# class Myclass2(Myclass1):
#     def __init__(self, name, age):
#         super().__init__(name, age)

# mc2=Myclass2("kamal",30)
# mc2.printuv()

















# class Myclass1:
#     def __init__(self,name,age) :
#         self.uname1=name
#         self.uage1=age
#     def printuv(self):
#         print("user name is ",self.uname1,"\nuser age is ",self.uage1,)
        
# class Myclass2(Myclass1):
#     def __init__(self, name, age):
#         Myclass1.__init__(self,name, age)
#         self.mobilenumber="1234567890"

# mc2=Myclass2("kamal",30)
# mc2.printuv()
# print(mc2.mobilenumber)

























# class Myclass1:
#     def __init__(self,name,age) :
#         self.uname1=name
#         self.uage1=age
#     def printuv(self):
#         print("user name is ",self.uname1,"\nuser age is ",self.uage1,)
        
# class Myclass2(Myclass1):
#     def __init__(self, name, age,mn):
#         Myclass1.__init__(self,name, age)
#         self.mobilenumber=mn

# mc2=Myclass2("kamal",30,9876543210)
# mc2.printuv()
# print(mc2.mobilenumber)

























# class Myclass1:
#     def __init__(self,name,age) :
#         self.uname1=name
#         self.uage1=age
#     def printuv(self):
#         print("user name is ",self.uname1,"\nuser age is ",self.uage1,)
        
# class Myclass2(Myclass1):
#     def __init__(self, name, age,mn):
#         Myclass1.__init__(self,name, age)
#         self.mobilenumber=mn
#     def mc2fun2(self):
#         print("this is class 2 method and the value is")
#         print("the user name is ",self.uname1,"\nthe user age is ",self.uage1)
#         print("and user mobile number is ",self.mobilenumber)
        

# mc2=Myclass2("kamal",30,9876543210)
# mc2.printuv()
# print(mc2.mobilenumber)
# mc2.mc2fun2()



















# class Myclass1:
#     def __init__(self,name,age) :
#         self.uname1=name
#         self.uage1=age
#     def printuv(self):
#         print("user name is ",self.uname1,"\nuser age is ",self.uage1,)
        
# class Myclass2(Myclass1):
#     def __init__(self, name, age,mn):
#         Myclass1.__init__(self,name, age)
#         self.mobilenumber=mn
#     def mc2fun2(self):
#         print("this is class 2 method and the value is")
#         print("the user name is ",self.uname1,"\nthe user age is ",self.uage1)
#         print("and user mobile number is ",self.mobilenumber)
        
# class Myclass3(Myclass2):
#     pass

# mc2=Myclass2("kamal",30,9876543210)
# mc2.printuv()
# print(mc2.mobilenumber)
# mc2.mc2fun2()
# print("_____________________________________________________")
# mc3=Myclass3("kamal",30,9876543210)
# mc3.printuv()
# print(mc3.mobilenumber)
# mc3.mc2fun2()
