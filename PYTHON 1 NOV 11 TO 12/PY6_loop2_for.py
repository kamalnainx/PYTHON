for f in range(5):
    print(f)


for f in range(5,10):
    print(f)



for f in range(5,19,1):
    print(f)



for f in range(5,19,2):
    print(f)








for f in range(4,19,2):
    if f == 10:
        continue
    print(f)






for f in range(4,19,2):
    if f == 10:
        break
    print(f)











for f in range(4,19,2):
    if f == 10:
        continue
    elif f == 16:
        break
    print(f)














for f in [0,1,2]:
    pass








for f in "hello":
    print(f)
    








for f in "hello","world":
    print(f)
    






for f in "hello world":
    print(f)








for f in ("hello","world"):
    print(f)








for f in ["hello","world"]:
    print(f)








d1={"h":"hello","w":"world"}
for f in d1:
    print(f)







d1={"h":"hello","w":"world"}
for f in d1:
    print(d1)







d1={"h":"hello","w":"world"}
for f in d1:
    print(d1[f])







d1={"h":"hello","w":"world"}
for f in d1:
    print(f ,d1[f])







d1={"h":"hello","w":"world"}
print(d1)
for f in d1:
    print(f ,":",d1[f])






d1={"h":"hello","w":"world"}
print(d1)
for f in d1.keys():
    print(f)
d1={"h":"hello","w":"world"}
print(d1)
for f in d1.values():
    print(f)
d1={"h":"hello","w":"world"}
print(d1)
for f in d1.items():
    print(f)






d1={"h":"hello","w":"world"}
print(d1)
for k,v in d1.items():
    print(k)
d1={"h":"hello","w":"world"}
print(d1)
for k,v in d1.items():
    print(v)
d1={"h":"hello","w":"world"}
print(d1)
for k,v in d1.items():
    print(k,v)
