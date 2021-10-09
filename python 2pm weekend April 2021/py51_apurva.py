# import pandas as pd
# import matplotlib.pyplot as plt

# item1 =  ["i",           "t",        "e",        "m",        "s",      "i"]
# date1=      ["2021/7/01",   "2021/7/01","2021/7/02","2021/7/02","2021/7/03",   "2021/7/1"]
# itemamount1=[10,            20,         25,         30,         50,      10]
# itemdic1=   [5.5,           12.5,       18.5,       20.21,      18.02,     33.33]

# df1={"amount":itemamount1,"dic":itemdic1}
# f=pd.DataFrame(data=df1, index=date1)

# # f.to_csv('file/dataclen1.csv')


# f.plot.bar( rot=45, title="ITEM DETAILS");

# plt.show(block=True);

































import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("file/dataclen1.csv")
# df=df.dropna()
# print(df)
amount= df["amount"]
print(amount)

listamount=[]
for x in amount:
    if x>0 or x<=0:
        listamount.append(int(x))
    else:        
        listamount.append(0)
print(listamount)


dic1= df["dic"]
listdic1=[]
for x in dic1:
    if x>0 or x<=0:
        listdic1.append(int(x))
    else:        
        listdic1.append(0)
print(listdic1)


# print( "amount ",amount,"     ",dic1)

item1 =  ["i",           "t",        "e",        "m",        "s",      "i",     "k"]
# date1=      ["2021/7/01",   "2021/7/01","2021/7/02","2021/7/02","2021/7/03",   "2021/7/1"]
# itemamount1=[10,            20,         25,         30,         50,      10]
# itemdic1=   [5.5,           12.5,       18.5,       20.21,      18.02,     33.33]

df1={"amount":listamount,"dic":listdic1}
f=pd.DataFrame(data=df1, index=item1)

f.plot.bar( rot=45, title="ITEM DETAILS");

plt.show(block=True);










