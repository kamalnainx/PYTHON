##import pandas as pd
##sd={"a":[10,20,30],
##    "b":[10,20,30],
##    "c":[10,20,30],
##    "d":[10,20,30],
##    "e":[10,20,30]
##    }
##sdf=pd.DataFrame(sd,index=["Hindi","Enflish","Maths"])
##print(sdf)










##import pandas as pd
##sd={" ":["Hindi","Enflish","Maths"],
##    "a":[10,20,30],
##    "b":[10,20,30],
##    "c":[10,20,30],
##    "d":[10,20,30],
##    "e":[10,20,30]
##    }
##for x in sd:
##    for y in sd[x]:
##        print(y,end=" ")
##    print()
















import pandas as pd
sd={
    "a":[10,20,30],
    "b":[10,20,30],
    "c":[10,20,30],
    "d":[10,20,30],
    "e":[10,20,30]
    }
sdf=pd.DataFrame(sd, index=["Hindi","Enflish","Maths"])
f=sdf.to_csv("file/sdf.csv")

f=open("file/sdf.csv","r")
print(f.read())
f.close()

pdf=pd.read_csv("file/sdf.csv")
print(pdf)
    
