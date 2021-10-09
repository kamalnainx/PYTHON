# list1=["apple","banana","cherry","date"]
# print(list1, type(list1))
# tuple1= tuple(list1)
# print(tuple1, type(tuple1))
# set1=set(tuple1)
# print(set1, type(set1))
# dic1={x:"Passed" for x in list1}
# print(dic1)

# x=10
# print(x, type(x))
# s=str(x)
# print(s, type(s))

# print("__________________________________________________________________________")





# dic1={key:value}


# dic1={"uname":"thekamalnain","uage":30,"uheight":6.1}
# print(dic1)









# dic1={"uname":"thekamalnain","uage":30,"uheight":6.1}
# print(dic1)
# print(dic1["uname"])
# print(dic1["uage"])
# print(dic1["uheight"])











# dic1={"uname":"thekamalnain","uage":30,"uheight":6.1, "uage":31}
# print(dic1)
# print(dic1["uname"])
# print(dic1["uage"])
# print(dic1["uheight"])















# dic1={"uname":"thekamalnain","uage":30,"uheight":6.1, "uage":31}
# print(dic1)
# print(len(dic1["uname"]))
# print(len(dic1))
















# dic1={"uname":"thekamalnain","uage":30,"uheight":6.1, "car":("bmw","ford"), "Mobile":["apple","samsung","one+"],"indian":True}
# print(dic1)

















# dic1={"uname":"thekamalnain","uage":30,"uheight":6.1, "car":("bmw","ford"), "Mobile":["apple","samsung","one+"],"indian":True}
# print(dic1)
# print(dic1, type(dic1))
# print(dic1["uname"], type(dic1["uname"]))
# print(dic1["uname"], type(dic1["uname"]))















# dic1={"uname":"thekamalnain","uage":30,"uheight":6.1, "car":("bmw","ford"), "mobile":["apple","samsung","one+"],"indian":True}
# print(dic1)
# print(dic1, type(dic1))
# print(dic1["uname"], type(dic1["uname"]))
# print(dic1["uage"], type(dic1["uage"]))
# print(dic1["uheight"], type(dic1["uheight"]))
# print(dic1["car"], type(dic1["car"]))
# print(dic1["mobile"], type(dic1["mobile"]))
# print(dic1["indian"], type(dic1["indian"]))











# data1={2000:1000,2005:2000,2010:4000,2015:8000,2020:1600}
# print(data1)








# data1={ 2000:{"h1":100,"h2":900},
#         2005:{"h1":200,"h2":1800},
#         2010:{"h1":400,"h2":3600},
#         2015:{"h1":800,"h2":7200},
#         2020:{"h1":100,"h2":900}
#        }
# print(data1)













# data1={ 2000:{"h1":100,"h2":900},
#         2005:{"h1":200,"h2":1800},
#         2010:{"h1":400,"h2":3600},
#         2015:{"h1":800,"h2":7200},
#         2020:{"h1":100,"h2":900}
#        }
# print(data1)
# print(data1[2005])












# data1={ 2000:{"h1":100,"h2":900},
#         2005:{"h1":200,"h2":1800},
#         2010:{"h1":400,"h2":3600},
#         2015:{"h1":800,"h2":7200},
#         2020:{"h1":100,"h2":900}
#        }
# print(data1)
# print(data1[2005])
# print(data1.get(2015))











# data1={ 2000:{"h1":100,"h2":900},
#         2005:{"h1":200,"h2":1800},
#         2010:{"h1":400,"h2":3600},
#         2015:{"h1":800,"h2":7200},
#         2020:{"h1":100,"h2":900}
#        }
# print(data1)
# print(data1[2005])
# print(data1.get(2015))
# x=data1.get(2005)
# print(x["h2"])









# data1={ 2000:900,2005:1800,2010:3600,2015:7200,2020:900}
# print(data1)
# print(data1.keys())
# print(data1.values())
# print(data1.items())





# data1={ 2000:900,2005:1800,2010:3600,2015:7200,2020:900}
# print(data1)

# for x in data1.keys():
#     print(x, end=" ")
# for x in data1.values():
#     print(x, end=" ")
# for x in data1.items():
#     print(x)
    











# data1={ 2000:900,2005:1800,2010:3600,2015:7200,2020:900}
# print(data1)
# data1[2000]=1000
# print(data1)

















# data1={ 2000:900,2005:1800,2010:3600,2015:7200,2020:900}
# print(data1)
# if 2010 in data1:
#     print("this value is in this list")














# data1={ 2000:900,2005:1800,2010:3600,2015:7200,2020:900}
# print(data1)
# if 2011 in data1:
#     print("this value is in this list")
# else:
#     print("this value is not in this list")    














# data1={ 2000:900,2005:1800,2010:3600,2015:7200,2020:900}
# print(data1)
# for x in data1.keys():
#     print(data1[x],end=" ")
#     data1[x]=input("please enter any value ")
#     print(x)
# print(data1)













# data1={ 2000:900,2005:1800,2010:3600,2015:7200,2020:900}
# print(data1)
# print(len(data1))
# for x in range(5,len(data1)):
#     print(data1[x],end=" ")
#     data1[x]=input("please enter any value ")
#     print(x)
# print(data1)











# wrong method
# data1={ 2000:900,2005:1800,2010:3600,2015:7200,2020:900}
# print(data1)
# print(len(data1))
# for x, y in range(0,len(data1) or data1.keys()):
#     if x<=0 or x>=4:
#         continue
#     print(x)
#     print(data1[y],end=" ")
#     data1[y]=input("please enter any value ")
#     print(y)
# print(data1)









# color1={"red":10,"green":20,"blue":30,"pink":40,"yellow":50}
# print(color1)
# color1["red"]=11
# print(color1)
















# color1={"red":10,"green":20,"blue":30,"pink":40,"yellow":50}
# print(color1)
# color1.update({"yellow":51})
# print(color1)

















# color1={"red":10,"green":20,"blue":30,"pink":40,"yellow":50}
# print(color1)
# color1["green"]=21
# print(color1)
# color1["gray"]=60
# print(color1)
# color1.update({"skyblue":70})
# print(color1)











# color1={"red":10,"green":20,"blue":30,"pink":40,"yellow":50}
# print(color1)
# color1.pop("pink")
# print(color1)
# color1.popitem()
# print(color1)














# color1={"red":10,"green":20,"blue":30,"pink":40,"yellow":50}
# print(color1)
# del color1["pink"]
# print(color1)
# color1.clear()
# print(color1)
# del color1
# print(color1)

# # print(color2)











# color1={"red":10,"green":20,"blue":30,"pink":40,"yellow":50}
# print(color1)
# color2=color1.copy()
# print(color2)















# color1=[["red",10],["green",20],["blue",30],["pink",40],["yellow",50]]
# print(color1)
# color2=dict(color1)
# print(color2)
















color1=[["red",10],["green",20],["blue",30],["pink",40],["yellow",50]]
print(color1)
tuple1=tuple(color1)
print(tuple1)
color2=dict(tuple1)
print(color2)
