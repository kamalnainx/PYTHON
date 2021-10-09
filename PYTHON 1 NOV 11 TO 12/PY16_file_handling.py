##f=open("files/demo1.txt")
##f=open("files/demo1.txt","rt")







##f=open("files/demo1.txt","w")
##f.write("remove old file and add this two.")
##f.close()







##f=open("files/demo1.txt","a")
##f.write("\nadd more data 3rd time in this file demo1.")
##f.close()






##f=open("files/demo1.txt","x")
##f.write("if file is there with same namethen get error, can't create new file")
##f.close()







##f=open("files/demo1.txt","r")
##print(f.read())
##f.close()






##f=open("files/demo1.txt","r")
##print(f.read(5))
##f.close()








##f=open("files/demo1.txt","r")
##print(f.readline())
##f.close()










##f=open("files/demo1.txt","r")
##for x in f:
##    print(x , end="")
##f.close()




'''
f=open("files/demo2.txt","x")
f.write("add your informetion.")
f.close()
'''


'''
import os
os.remove("files/demo2.txt")
'''




import os
if os.path.exists("files/demo1.txt"):
    os.remove("files/demo1.txt")
    os.rmdir("files")
    
else:
    print("this file path is not there")





