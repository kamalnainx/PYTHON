# class Mc1:
#     def __init__(self,age):
#         self.ua=age
#     def funcname(self):
#         print(self.ua)
# class Mc2(Mc1):
#     pass
# obj1=Mc2(10)
# obj1.funcname()










# class Mc1:
#     def __init__(self,age):
#         self.ua=age
#     def funcname(self):
#         print(self.ua)
# class Mc2(Mc1):
#     def __init__(self,age):
#         Mc1.__init__(self,age)
# obj1=Mc2(10)
# obj1.funcname()











# class Mc1:
#     def __init__(self,age):
#         self.ua=age
#     def funcname(self):
#         print(self.ua)
# class Mc2(Mc1):
#     def __init__(self,age):
#         super().__init__(age)
# obj1=Mc2(10)
# obj1.funcname()














# class Mc1:
#     def __init__(self,age):
#         self.ua=age
#     def funcname(self):
#         print(self.ua)
# class Mc2(Mc1):
#     def __init__(self,age):
#         super().__init__(age)
#         self.birthyear=2020-self.ua
# obj1=Mc2(10)
# obj1.funcname()
# print(obj1.birthyear)













class Mc1:
    def __init__(self,age):
        self.ua=age
    def funcname(self):
        print(self.ua)
class Mc2(Mc1):
    def __init__(self,age):
        super().__init__(age)
        self.birthyear=2020-self.ua
    def mc2fun1(self):
        print("this is my 1 function in class2 with user age",self.ua,"\n and user birth year is ",self.birthyear)
obj1=Mc2(10)
obj1.funcname()
print(obj1.birthyear)
obj1.mc2fun1()