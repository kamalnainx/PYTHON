# x=100
# print(x)







# x=100
# def myfun1():
#     print("inside of function",x)
# myfun1()
# print("call x out side of function ",x)
















# def myfun1():
#     x=100
#     print("inside of function",x)
# myfun1()
# print("call x out side of function ",x) # error local inside of function.














# x=200
# def myfun1():
#     x=100
#     print("inside of function",x)
# myfun1()
# print("call x out side of function ",x)














# x="yellow"
# def myfun1():
#     x="red"           #inside of function is local var.
#     print("inside of function",x)
#     def imf():
#         print(x)
#     imf()
# myfun1()
# print("call x out side of function ",x)























# def myfun1():
#     x="red"           #inside of function is local var.
#     print("inside of function",x)
#     def imf():
#         print(x)
#     imf()
# myfun1()
# print("call x out side of function ",x) #color is not there.




















# def myfun1():
#     global x
#     x="red"           #inside of function is local var.
#     print("inside of function",x)
#     def imf():
#         print(x)
#     imf()
# myfun1()
# print("call x out side of function ",x) #color is not there.




















x="yellow"
def myfun1():
    global x
    x="red"           #inside of function is local var.
    print("inside of function",x)
    def imf():
        print(x)
    imf()
myfun1()
x="pink"
print("call x out side of function ",x) 
