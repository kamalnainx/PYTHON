##import pandas
##
##a=[2,5,9,2,5,9,9,2,5]
##print(a)
##d=pandas.Series(a)
##print(d)
##print(d[1])
##print(d[1:6])
##print(d[1:6:2])







##
##import pandas as pd
##a=[2,5,9,5]
##d=pd.Series(a)
##print(d)
##di=pd.Series(a,index=["x","y","z","aa"])
##print(di)
##print(di["z"])










##
##import pandas as pd
##
##print("list",pd.Series([2,5,9,5]))
##print("list",pd.Series([2,5,9,5],index=["x","y","z","aa"]))
##print("tuple",pd.Series((2,5,9,5)   ))
##print("tuple",pd.Series((2,5,9,5)   ,index=["x","y","z","aa"]))
##print("dic",pd.Series({2:5,9:5} ))
##print("dic",pd.Series({2:5,9:5},index=["x","y","z","aa"]))







##import pandas as pd
##year={"jan":31,"feb":28,"march":31,"april":30,"may":31,"jun":30}
##y=pd.Series(year)
##print(y)
##print(pd.Series(year,index=["jan","feb","march"]))









import pandas as pd
week={"jan":[2,9,16,23,30],"feb":[7,14,21,28],"march":[7,14,21,28],"april":30,"may":31,"jun":30}
y=pd.Series(week)
print(y)
print(pd.Series(week,index=["jan","feb","march"]))
print(pd.Series(week["jan"]))

