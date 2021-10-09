# what is function?
# a function is a block of code by user .
# function dispaly only when it's called by user;

# def myfun1():
#     pass


# if 10>5:
#     pass




# def myfun1():
#     print("hello world")

# myfun1()










# var1=10
# var2=10
# var3=10

# print(var1,var2,var3)
# print(var1,var2,var3)
# print(var1,var2,var3)

# print(var1,var2,var3)
# print(var1,var2,var3)
# print(var1,var2,var3)














# def fun1():
#     var1=10
#     var2=20
#     var3=30

#     print(var1,var2,var3)
#     print(var1,var2,var3)
#     print(var1,var2,var3)

# fun1()
# fun1()
# fun1()
























# def fun1(    var1=10, var2=20, var3=30):
#     print(var1,var2,var3)
#     print(var1,var2,var3)
#     print(var1,var2,var3)

# fun1()
# fun1()
# fun1()






















# def fun1(    var1=10, var2=20, var3=30):
#     print(var1,var2,var3)
#     print(var1,var2,var3)
#     print(var1,var2,var3)

# fun1(1,2,3)
# fun1(11,22,33)
# fun1(0,00,000)






















# def fun1(    var1=10, var2=20, var3=30):
#     print(var1,var2,var3)
#     print(var1,var2,var3)
#     print(var1,var2,var3)

# fun1(1,2)
# fun1(11,)
# fun1(0,00,000)
# fun1()






# def myfun1(name1, age, height):
#     print("user name =",name1,"user age is=",age,"user height=",height)
# myfun1(30,6.1,"kamal nain")













# def myfun1(name1, age, height):
#     print("user name =",name1,"user age is=",age,"user height=",height)
# myfun1(age=30,height=6.1,name1="kamal nain")





# def myfun1(name1, age, height):
#     print("user name =",name1,"user age is=",age,"user height=",height)
# myfun1(age="30",height="six.one",name1="kamal nain")


















# def myfun1(name1, age, height):
#     age+=10
#     print("user name =",name1,"user age is=",age,"user height=",height)
# myfun1(age=30,height="six.one",name1="kamal nain")

















# def myfun1(name1, age, height):
#     age+=10
#     print("user name =",name1,"user age is=",age,"user height=",height)
# age1=input("what is your age")    
# myfun1(age=age1,height="six.one",name1="kamal nain")














# def myfun1(name1, age, height):
#     age+=10
#     print("user name =",name1,"user age is=",age,"user height=",height)

# myfun1(age=30,height="six.one",name1="kamal nain")
















# def myfun1(*user1):
#     print("user name =",user1[2],"user age is=",user1[0],"user height=",user1[1])

# myfun1(30,"six.one","kamal nain")










# def myfun1(**user1):
#     print("user name =",user1["name1"],"user age is=",user1["age"],"user height=",user1["height"])

# myfun1(age=30,height="six.one",name1="kamal nain")











# def myfun1(user1):
#     print("user name =",user1["name1"],"user age is=",user1["age"],"user height=",user1["height"])
# dic1={"age":30,"height":"six.one","name1":"kamal nain"}
# myfun1(dic1)
















# def myfun1(user1):
    
#     for x in user1:
#         print(x)
# dic1={"age":30,"height":"six.one","name1":"kamal nain"}
# myfun1(dic1)
























# def myfun1():
#     return "hello world"
# print(myfun1())


















# def myfun1(f):
#     return f*f
# print(myfun1(22))
















# def myfun1():
#     print("hello world")
#     myfun1()
# myfun1()

























# v1=1
# def myfun1():
#     global v1
#     print("hello world",v1)
#     v1+=1
#     myfun1()
# myfun1()














# import sys
# sys.setrecursionlimit(3000)
# v1=1
# def myfun1():
#     global v1
#     print("hello world",v1)
#     v1+=1
#     myfun1()
# myfun1()





















# import sys
# sys.setrecursionlimit(3000)
# print(sys.getrecursionlimit())
# v1=1
# def myfun1():
#     global v1
#     print("hello world",v1)
#     v1+=1
#     myfun1()
# myfun1()




















# import sys
# sys.setrecursionlimit(30)
# print(sys.getrecursionlimit())
# v1=1
# def myfun1():
#     global v1
#     print("hello world",v1)
#     v1+=1
#     myfun1()
# myfun1()






















# def myfun1(n):
#     if(n>0):
#         finaloutput=myfun1(n-1)
#         print(n)
# myfun1(5)























# def myfun1(n):
#     if(n<=10):
#         myfun1(n+1)
#         print(n) #1 ,2 ,3,4,5,6,7,8,9,10 = fifo
# myfun1(1)















# def myfun1(n):
#     if(n>0):
#         myfun1(n-1)
#         print(n)
# myfun1(10)














def myfun1(k):
    if(k>=1):
        ot1=k*myfun1(k-1)
        print(ot1)
    else:
        ot1=1
    return ot1 
myfun1(5)