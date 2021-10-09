# x=10
# print(x)







# print(x)








# x=10
# try:
#     print(x)
# except:
#     print("x not found.")
















# try:
#     print(x)
# except NameError:
#     print("var name is not found")
















# try:
#     print(x)
# except NameError:
#     print("var name is not found")
# except:
#     print("other error")    























# x=1/0
# try:
#     print(x)
# except NameError:
#     print("var name is not found")
# except:
#     print("other error")    















# try:
#     x=1/0
#     print(x)
# except NameError:
#     print("var name is not found")
# except:
#     print("other error")    












# try:
#     x=1
#     print(x)
# except NameError:
#     print("var name is not found")
# except:
#     print("other error")    
# else:
#     print("nothing is wrong")

















# try:
#     x=1/0
#     print(x)
# except NameError:
#     print("var name is not found")
# except:
#     print("other error")    
# else:
#     print("nothing is wrong")
# finally:
#     print("try except is finished")





n1=[1,2,3,4,0,12,3]
for f in n1:
    try:
        x=1/f
        print(x , end="     ")
    except:
        continue    
