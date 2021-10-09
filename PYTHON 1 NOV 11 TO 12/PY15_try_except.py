# x=10
# print(x)







# x
# print(x)



# try:
#     print(x)
# except:
#     print("name 'x' is not defined")






# try:
#     print(x)
# except NameError:
#     print("name 'x' is not defined")
# except:
#     print("something not right")








# x=10
# try:
#     print(x)
# except NameError:
#     print("name 'x' is not defined")
# except:
#     print("something not right")
# else:
#     print("no error")














# try:
#     print(x)
# except NameError:
#     print("name 'x' is not defined")
# except:
#     print("something not right")
# else:
#     print("no error")
# finally:
#     print("try - except is over")
    







from os import write


try:
    x=open("demofile/demo1.txt")
    x=write("lorem ipsum")
except NameError:
    print("name 'x' is not defined")
except:
    print("something not right in this file")
else:
    print("no error")
finally:
    print("try - except is over")

