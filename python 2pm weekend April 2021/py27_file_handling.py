# a=append
# x=create
# w=over write

# f=open("file/demo1.txt","x")
# f.close()



# f=open("file/demo1.txt","x")
# f.write("this is my first file.")
# f.close()

f=open("file/demo1.csv","x")
f.write("item , month1,month2,month3\n")
f.write("item , 10,20,30\n")
f.write("item , 11,22,33\n")
f.write("item , 100,200,300\n")
f.close()













# f=open("file/demo1.txt","a")
# f.write("\nthis is my 2nd line in this file file.")
# f.close()




# f=open("file/demo1.txt","a")
# f.write("\nhello world")
# f.close()













# f=open("file/demo1.txt","w")
# f.write("\nthis is overwrite line in this file.")
# f.close()


























# # r=read
# f=open("file/demo1.txt","r")
# x=f.read()
# print(x)
# f.close()

# f=open("file/demo2.txt","x")
# f.write(x)
# f.close()



# f=open("file/demo1.txt","r")
# x=f.read()
# print(x)
# f.close()

# f=open("file/demo1.txt","a")
# f.write(x)
# f.close()















# f=open("file/demo1.txt","r")
# x=f.read(7)
# print(x)
# f.close()















# # r=read
# f=open("file/demo1.txt","r")
# x=f.readline()
# x+=f.readline()
# print(x)
# f.close()














# r=read
# f=open("file/demo1.txt","r")
# x=f.readline()
# x+=f.readline()
# x+=f.readline()
# x+=f.readline()
# x+=f.readline()
# x+=f.readline()
# print(x)
# f.close()




















# f=open("file/demo1.txt","r")
# for x in f:
#     print(x)
# f.close()
















# import os
# if os.path.exists("file/demo1.txt"):
#     os.remove("file/demo1.txt")
# else:
#     print("wrong path or file is does not exist")    
