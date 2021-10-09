##import pandas as pd
##students={"ram":[1,2,3,4,5],
##          "sham":[11,22,33,44,55],
##          "ghansham":[10,20,30,40,50]         
##          }
##print(students)
##df=pd.DataFrame(students)
##print(df)







##
##import pandas as pd
##students={"ram":[1,2,3,4,5],
##          "sham":[11,22,33,44,55],
##          "ghansham":[10,20,30,40,50]         
##          }
##print(students)
##df=pd.DataFrame(students)
##print(df)
##print(df.loc[1])
##df=pd.DataFrame(students["sham"])
##print(df)












##
##import pandas as pd
##students={"ram":[1,2,3,4,5],
##          "sham":[11,22,33,44,55],
##          "ghansham":[10,20,30,40,50]         
##          }
##print(students)
##df=pd.DataFrame(students)
##print(df)
##print(df.loc[1])
##print(df.loc[[1,2]])












##
##import pandas as pd
##students={"ram":[1,2,3,4,5],
##          "sham":[11,22,33,44,55],
##          "ghansham":[10,20,30,40,50]         
##          }
##print(students)
##df=pd.DataFrame(students)
##print(df)
##print(df.loc[1])
##print(df.loc[[1,2]])











##
##import pandas as pd
##students={"ram":[1,2,3,4,5],
##          "sham":[11,22,33,44,55],
##          "ghansham":[10,20,30,40,50]         
##          }
##il=["Maths","English","hindi","G.K","music"]
##print(students)
##df=pd.DataFrame(students, index=il)
##print(df)











import pandas as pd
students={"ram":[1,2,3,4,5],
          "sham":[11,22,33,44,55],
          "ghansham":[10,20,30,40,50]         
          }
il=["Maths","English","hindi","G.K","music"]
print(students)
df=pd.DataFrame(students, index=il)
print(df)
print(df.loc["hindi"])
