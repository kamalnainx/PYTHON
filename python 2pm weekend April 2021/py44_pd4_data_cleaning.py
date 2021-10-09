# data cleaning
# 1 empty data/cell
# 2 data in wrong format
# 3 wrong data entry
# 4 duplicates




# f=open("file/dataclean.csv","w")
# x="s_no, items, Date, price, dic\n"
# x+="1, i, 2021/7/01, 10, 12.5\n"
# x+="2, t, 2021/7/01, 20, 5.5\n"
# x+="3, e, 2021/7/01, 30, 18.5\n"
# x+="4, m, 2021/7/01, 40, 10.1\n"
# x+="5, , 2021/7/02,  , \n"
# x+="6, i,           , 10,  12.5\n"
# x+="7, t, 2021/7/02, 20, 5.5\n"
# x+="8, e, 2021/7/03, 30, 8.5\n"
# x+="9, m, 2021/7/03, 40, 10.1\n"
# x+="10, s, 2021/7/03, 50, 32.33\n"
# x+="11, ,2021/7/03,  ,  ,\n"

# f.write(x)
# f.close()
























# import pandas as pd

# itemname1=  ["i",           "t",        "e",        "m",        "s",        " ",    "i"]
# date1=      ["2021/7/01",   "2021/7/01","2021/7/02","2021/7/02","2021/7/03"," ",    "2021/7/1"]
# itemamount1=[10,            20,         25,         30,         50,         "",     10]
# itemdic1=   [5.5,           12.5,       18.5,       20.21,      "",         "",     33.33]

# df1={"item":itemname1,"date":date1,"amount":itemamount1,"dic":itemdic1}
# f=pd.DataFrame(df1)

# print(f)

# f.to_csv('file/dataclen1.csv')







































# empty cell data hide
# import pandas as pd

# df=pd.read_csv("file/dataclen1.csv")

# # print(df.to_string())

# ndf=df.dropna()

# print(ndf.to_string())








































# import pandas as pd

# df=pd.read_csv("file/dataclen1.csv")


# df.dropna(inplace=True)

# print(df.to_string())










































# import pandas as pd

# df=pd.read_csv("file/dataclen1.csv")


# df.fillna(150,inplace=True)

# print(df.to_string())










































# import pandas as pd

# df=pd.read_csv("file/dataclen1.csv")


# df['date']=pd.to_datetime(df['date'])

# print(df.to_string())










































# import pandas as pd

# df=pd.read_csv("file/dataclen1.csv")


# df['date']=pd.to_datetime(df['date'])
# df.dropna(subset=['date'],inplace=True)

# print(df.to_string())









































# import pandas as pd

# df=pd.read_csv("file/dataclen1.csv")

# df.loc[4,'item']="lock"

# print(df.to_string())












































# import pandas as pd

# df=pd.read_csv("file/dataclen1.csv")

# for x in df.index:
#     if df.loc[x,"amount"]>25:
#         df.loc[x,"amount"]=32


# print(df.to_string())







































# import pandas as pd

# df=pd.read_csv("file/dataclen1.csv")

# for x in df.index:
#     if df.loc[x,"amount"]>25:
#         df.drop(x,inplace=True)


# print(df.to_string())








































# import pandas as pd

# df=pd.read_csv("file/dataclen1.csv")



# print(df.duplicated())











































# import pandas as pd

# df=pd.read_csv("file/dataclen1.csv")

# df.drop_duplicates(inplace=True)

# print(df.to_string())



















