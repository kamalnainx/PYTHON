# import matplotlib.pyplot as plt
# plt.plot([1,3,5],[1,5,2])
# plt.show()






# import matplotlib.pyplot as plt
# x=[1,3,5]
# y=[1,5,2]
# plt.plot(x,y)
# plt.show()
















# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([1,3,5])
# y=np.array([1,5,2])
# plt.plot(x,y)
# plt.show()













# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# plt.plot(x,y)
# plt.show()














# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# plt.plot(x,y,"o")
# plt.show()















# import matplotlib.pyplot as plt
# import numpy as np
# # x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# plt.plot(y,"--")
# plt.show()























# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# plt.plot(y,marker="o")
# plt.show()


































# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# plt.plot(x,y,marker="*")
# plt.show()

# # marker=   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--






















# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# plt.plot(x,y, "D:r")
# plt.show()

# # marker=   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# #color=     r,g,b,c,m,y,bl,w































# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# plt.plot(x,y, "D-.k")
# plt.show()

# # marker|line|color
# # marker    =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color     =   r,g,b,c,m,y,k,w
# #line       =   -,:,--,-.







































# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# plt.plot(x,y, "-.k",marker='H', ms=25)
# plt.show()

# # marker|line|color
# # marker        =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color         =   r,g,b,c,m,y,k,w
# # line          =   -,:,--,-.
# # markersize    =   ms


















# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# plt.plot(x,y, "-.",marker='H', ms=25, mec="r", mfc="b" )
# plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w
# # line              =   -,:,--,-.
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc


























# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# plt.plot(x,y, marker='^', ms=25, mec="#ff0000", mfc="green", linestyle="dotted")
# plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w/ hexadecimal color #000000 to #ffffff/ by name
# # line              =   -,      :,      --,     -.      
# # line style        =   solid,  dotted, dashed, dashdot, none
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc



































# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# plt.plot(x,y, marker='^', ms=25, mec="#ff0000", mfc="green", ls="-.",color="r")
# plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w/ hexadecimal color #000000 to #ffffff/ by name
# # line              =   -,      :,      --,     -.      
# # line style        =   solid,  dotted, dashed, dashdot, none/ ls=":"
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc



































# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# plt.plot(x,y, marker='^', ms=25, mec="#ff0000", mfc="green", ls="-.",c="r", lw="3")
# plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w/ hexadecimal color #000000 to #ffffff/ by name
# # line              =   -,      :,      --,     -.      
# # line style        =   solid,  dotted, dashed, dashdot, none/ ls=":"
# # line width        =   lw="n"
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc


































# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# plt.plot(x,y, marker='^', ms=25, mec="#ff0000", mfc="green", ls="-.",c="r", linewidth="3")
# plt.plot(y,x, marker='v', ms=25, mec="#ff0000", mfc="yellow", ls="-.",c="y", linewidth="3")

# plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w/ hexadecimal color #000000 to #ffffff/ by name
# # line              =   -,      :,      --,     -.      
# # line style        =   solid,  dotted, dashed, dashdot, none/ ls=":"
# # line width        =   lw="n"
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc
































# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# x1=np.array([50,33,66,33,66,50])
# y1=np.array([95,3,66,66,3,95])
# plt.plot(x,y,x1,y1, marker='^', ms=25, mec="#ff0000", mfc="green", ls="-.",c="r", linewidth="3")
# plt.plot(y,x, marker='v', ms=25, mec="#ff0000", mfc="yellow", ls="-.",c="y", linewidth="3")

# plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w/ hexadecimal color #000000 to #ffffff/ by name
# # line              =   -,      :,      --,     -.      
# # line style        =   solid,  dotted, dashed, dashdot, none/ ls=":"
# # line width        =   lw="n"
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc






























# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# x1=np.array([50,33,66,33,66,50])
# y1=np.array([95,3,66,66,3,95])
# plt.plot(x,y,x1,y1, marker='^', ms=25, mec="#ff0000", mfc="green", ls="-.",c="r", linewidth="3")
# plt.plot(y,x, marker='v', ms=25, mec="#ff0000", mfc="yellow", ls="-.",c="y", linewidth="3")
# plt.xlabel("x lable")
# plt.ylabel("y lable")

# plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w/ hexadecimal color #000000 to #ffffff/ by name
# # line              =   -,      :,      --,     -.      
# # line style        =   solid,  dotted, dashed, dashdot, none/ ls=":"
# # line width        =   lw="n"
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc




























# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# x1=np.array([50,33,66,33,66,50])
# y1=np.array([95,3,66,66,3,95])
# plt.plot(x,y,x1,y1, marker='^', ms=25, mec="#ff0000", mfc="green", ls="-.",c="r", linewidth="3")
# plt.plot(y,x, marker='v', ms=25, mec="#ff0000", mfc="yellow", ls="-.",c="y", linewidth="3")
# plt.xlabel("x lable")
# plt.ylabel("y lable")
# plt.title("plot chart")
# plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w/ hexadecimal color #000000 to #ffffff/ by name
# # line              =   -,      :,      --,     -.      
# # line style        =   solid,  dotted, dashed, dashdot, none/ ls=":"
# # line width        =   lw="n"
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc
# # label             =   xlabel, ylabel, title



























# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# x1=np.array([50,33,66,33,66,50])
# y1=np.array([95,3,66,66,3,95])

# plt.plot(x,y, marker='^', ms=25, mec="#ff0000", mfc="green", ls="-.",c="r", linewidth="3")
# plt.plot(y1,x1, marker='v', ms=25, mec="#ff0000", mfc="yellow", ls="-.",c="y", linewidth="3")
# font1title={"family":"Algerian","color":"green","size":30}
# font2xy={"family":"Cooper","color":"blue","size":15}

# plt.xlabel("x lable",fontdict=font2xy )
# plt.ylabel("y lable",fontdict=font2xy )
# plt.title("plot chart",fontdict=font1title )
# plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w/ hexadecimal color #000000 to #ffffff/ by name
# # line              =   -,      :,      --,     -.      
# # line style        =   solid,  dotted, dashed, dashdot, none/ ls=":"
# # line width        =   lw="n"
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc
# # label             =   xlabel, ylabel, title























# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# x1=np.array([50,33,66,33,66,50])
# y1=np.array([95,3,66,66,3,95])

# plt.plot(x,y, marker='^', ms=25, mec="#ff0000", mfc="green", ls="-.",c="r", linewidth="3")
# plt.plot(y1,x1, marker='v', ms=25, mec="#ff0000", mfc="yellow", ls="-.",c="y", linewidth="3")
# font1title={"family":"Algerian","color":"green","size":30}
# font2xy={"family":"Cooper","color":"blue","size":15}

# plt.xlabel("x lable",fontdict=font2xy )
# plt.ylabel("y lable",fontdict=font2xy )
# plt.title("plot chart",fontdict=font1title, loc="right")
# plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w/ hexadecimal color #000000 to #ffffff/ by name
# # line              =   -,      :,      --,     -.      
# # line style        =   solid,  dotted, dashed, dashdot, none/ ls=":"
# # line width        =   lw="n"
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc
# # label             =   xlabel, ylabel, title
# # fontdict          =   ex:- {"family":"Algerian","color":"green","size":30}
# # position          =   loc=left, right, center





















# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# x1=np.array([50,33,66,33,66,50])
# y1=np.array([95,3,66,66,3,95])

# plt.plot(x,y, marker='^', ms=25, mec="#ff0000", mfc="green", ls="-.",c="r", linewidth="3")
# plt.plot(y1,x1, marker='v', ms=25, mec="#ff0000", mfc="yellow", ls="-.",c="y", linewidth="3")
# font1title={"family":"Algerian","color":"green","size":30}
# font2xy={"family":"Cooper","color":"blue","size":15}

# plt.xlabel("x lable",fontdict=font2xy )
# plt.ylabel("y lable",fontdict=font2xy )
# plt.title("plot chart",fontdict=font1title, loc="right")

# plt.grid()
# plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w/ hexadecimal color #000000 to #ffffff/ by name
# # line              =   -,      :,      --,     -.      
# # line style        =   solid,  dotted, dashed, dashdot, none/ ls=":"
# # line width        =   lw="n"
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc
# # label             =   xlabel, ylabel, title
# # fontdict          =   ex:- {"family":"Algerian","color":"green","size":30}
# # position          =   loc=left, right, center



















# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# x1=np.array([50,33,66,33,66,50])
# y1=np.array([95,3,66,66,3,95])

# plt.plot(x,y, marker='^', ms=25, mec="#ff0000", mfc="green", ls="-.",c="r", linewidth="3")
# plt.plot(y1,x1, marker='v', ms=25, mec="#ff0000", mfc="yellow", ls="-.",c="y", linewidth="3")
# font1title={"family":"Algerian","color":"green","size":30}
# font2xy={"family":"Cooper","color":"blue","size":15}

# plt.xlabel("x lable",fontdict=font2xy )
# plt.ylabel("y lable",fontdict=font2xy )
# plt.title("plot chart",fontdict=font1title, loc="right")

# plt.grid(axis="x")
# plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w/ hexadecimal color #000000 to #ffffff/ by name
# # line              =   -,      :,      --,     -.      
# # line style        =   solid,  dotted, dashed, dashdot, none/ ls=":"
# # line width        =   lw="n"
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc
# # label             =   xlabel, ylabel, title
# # fontdict          =   ex:- {"family":"Algerian","color":"green","size":30}
# # position          =   loc=left, right, center
# # grid              =   grid() | grid(axis="x") | grid(axis="y")


















# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([50,33,66,33,66,50])
# y=np.array([95,3,66,66,3,95])
# x1=np.array([50,33,66,33,66,50])
# y1=np.array([95,3,66,66,3,95])

# plt.plot(x,y, marker='^', ms=25, mec="#ff0000", mfc="green", ls="-.",c="r", linewidth="3")
# plt.plot(y1,x1, marker='v', ms=25, mec="#ff0000", mfc="yellow", ls="-.",c="y", linewidth="3")
# font1title={"family":"Algerian","color":"green","size":30}
# font2xy={"family":"Cooper","color":"blue","size":15}

# plt.xlabel("x lable",fontdict=font2xy )
# plt.ylabel("y lable",fontdict=font2xy )
# plt.title("plot chart",fontdict=font1title, loc="right")

# plt.grid(axis="y")
# plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w/ hexadecimal color #000000 to #ffffff/ by name
# # line              =   -,      :,      --,     -.      
# # line style        =   solid,  dotted, dashed, dashdot, none/ ls=":"
# # line width        =   lw="n"
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc
# # label             =   xlabel, ylabel, title
# # fontdict          =   ex:- {"family":"Algerian","color":"green","size":30}
# # position          =   loc=left, right, center
# # grid              =   grid() | grid(axis="x") | grid(axis="y")


















import matplotlib.pyplot as plt
import numpy as np
x=np.array([50,33,66,33,66,50])
y=np.array([95,3,66,66,3,95])
x1=np.array([50,33,66,33,66,50])
y1=np.array([95,3,66,66,3,95])

plt.plot(x,y, marker='^', ms=25, mec="#ff0000", mfc="green", ls="-.",c="r", linewidth="3")
plt.plot(y1,x1, marker='v', ms=25, mec="#ff0000", mfc="yellow", ls="-.",c="y", linewidth="3")
font1title={"family":"Algerian","color":"green","size":30}
font2xy={"family":"Cooper","color":"blue","size":15}

plt.xlabel("x lable",fontdict=font2xy )
plt.ylabel("y lable",fontdict=font2xy )
plt.title("plot chart",fontdict=font1title, loc="right")

plt.grid(color="black",linestyle="--",linewidth="1")
plt.show()

# # marker|line|color
# # marker            =   o,*,., ',' ,x,X,+,P,s,D,d,p,H,h,v,^,<,>,1,2,3,4,|,_,--
# # color             =   r,g,b,c,m,y,k,w/ hexadecimal color #000000 to #ffffff/ by name
# # line              =   -,      :,      --,     -.      
# # line style        =   solid,  dotted, dashed, dashdot, none/ ls=":"
# # line width        =   lw="n"
# # markersize        =   ms
# # matkerefgecolor   =   mec
# # markerfacecolor   =   mfc
# # label             =   xlabel, ylabel, title
# # fontdict          =   ex:- {"family":"Algerian","color":"green","size":30}
# # position          =   loc=left, right, center
# # grid              =   grid() | grid(axis="x") | grid(axis="y") 
# # grid property     =   grid(color:"",linestyle="",linewidth="")




































import numpy as np
arr1=np.array([[10,6,8,2,4],[1,9,3,7,5]])

arr2=[]
list=[]
for x in arr1:
    y = np.flip(x)
    arr2.append(y)
print("Seperate arrays in list = ",arr2)
arr1=np.concatenate((arr2[0],arr2[1])).reshape(2,5)
print(arr1)
# for x in arr2:
#     for y in x:
#         list.append(y)   
# print("\n")
# arr3=np.array(list)
# print(arr3.reshape(2,5))