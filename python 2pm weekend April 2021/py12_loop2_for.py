# for varname addvalue(in) range(start,stop,step)




# print(range(10))








# for x in range(10):
#     print(x)













# for x in range(1,10):
#     print(x)








# for x in range(1,10,1):
#     print(x, end="\t")
# print()
# for x in range(0,10,2):
#     print(x, end="\t")















# for x in range(5,51,5):
#     print(x, end="\t")
# else:
#     print("end of table")
















dic1={"apple":200,"banana":80,"cherry":180}
for x in dic1:
    print(x, end="\t")
print()
for x in dic1:
    print(dic1[x], end="\t")
print()
for x in dic1.items():
    print(x, end="\t")
print()
for x,y in dic1.items():
    print("item=(",x,":",y,")  keys=",x,"values:",y,  end="\t")
print()

for x in dic1.values():
    print(x, end="\t")
print()
for x in dic1.keys():
    print(x, end="\t")
