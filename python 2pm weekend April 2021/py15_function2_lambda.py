# lambda syntax
# lambda arguments:Exception


# print(lambda :"helloworld")




# x=lambda : "hello world"
# print(x())








# x=lambda a: a
# print(x("hello world"))








# x=lambda a: a+" 10"
# print(x("hello world"))








# x=lambda a,b,c: a+b*c
# print(x(1,10,20))


















# def myfun1():
#     x= lambda a:a
#     print(x(1))
# myfun1()
















# def myfun1():
#     return lambda a:a
# x=myfun1() #function call
# print(x(1)) #lambda call















# def myfun1(b):
#     return lambda a:a+b
# x=myfun1(2)
# print(x(1))











# def x(): xyz
# x()
# x()
# x()
# x()











def myfun1(b):
    return lambda a:a+b

x=myfun1(2)
print(x(1))

x=myfun1(22)
print(x(11))
