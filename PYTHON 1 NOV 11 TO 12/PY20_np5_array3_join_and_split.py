##import numpy as np
##a1=np.array([2,4,6,8])
##a2=np.array([2,4,6,8])
##print(a1,a2)
##print(a1+a2)
##print(np.concatenate((a1,a2)))










##
##import numpy as np
##a1=np.array([2,4,6,8])
##a2=np.array([2,4,6,8])
##print(a1,a2)
##print(a1+a2)
##x=np.concatenate((a1,a2))
##print(x)











##import numpy as np
##a1=np.array([   [2,4,6,8]   ,   [2,4,6,8]   ])
##a2=np.array([   [2,4,6,8]   ,   [2,4,6,8]   ])
##print(a1,"\n",a2)
##x=np.concatenate((a1,a2))
##print(x)
##x=np.concatenate((a1,a2),axis=1)
##print(x)











##import numpy as np
##a1=np.array([   [2,4,6,8]   ,   [2,4,6,8]   ])
##a2=np.array([   [2,4,6,8]   ,   [2,4,6,8]   ])
##print(a1,"\n",a2)
##x=np.concatenate((a1,a2))
##print(x)
##x=np.concatenate((a1,a2),axis=1)
##print(x)









##import numpy as np
##a1=np.array([2,4,6,8])
##a2=np.array([2,4,6,8])
##print(a1,"\n",a2)
##x=np.concatenate((a1,a2))
##print(x)
##x=np.stack((a1,a2),axis=1)
##print(x)










##import numpy as np
##a1=np.array([2,4,6,8])
##a2=np.array([2,4,6,8])
##print(a1,"\n",a2)
##x=np.concatenate((a1,a2))
##print(x)
##x=np.hstack((a1,a2))
##print("hstack",x)
##x=np.vstack((a1,a2))
##print("vstack",x)
##x=np.dstack((a1,a2))
##print("dstack",x)









print("------------------------------------------------------------")






##import numpy as np
##a=np.array([1,2,3,4,5,6])
##print(a)
##print(np.array_split(a,3))












##import numpy as np
##a=np.array([1,2,3,4,5,6])
##print(a)
##s=np.array_split(a,2)
##print(s)
##s=np.array_split(a,3)
##print(s)
##s=np.array_split(a,4)
##print(s)









##
##import numpy as np
##a=np.array([1,2,3,4,5,6])
##print(a)
##s=np.array_split(a,2)
##print(s)
##print(s[0])
##print(s[1])
##s=np.array_split(a,3)
##print(s[0])
##print(s[1])
##print(s[2])
##print(s)












##
##import numpy as np
##a=np.array([[1,2],[1,2],[3,4],[3,4],[5,6],[5,6]])
##print(a)
##s=np.array_split(a,2)
##print(s)
##print(s[0])
##print(s[1])
##s=np.array_split(a,3)
##print(s[0])
##print(s[1])
##print(s[2])
##print(s)













import numpy as np
a=np.array([[1,2,3],[4,5,6],[1,2,3],[4,5,6],[1,2,3],[4,5,6]])
print(a)
s=np.array_split(a,3)
print(s)
s=np.array_split(a,3,axis=1)
print(s)
s=np.hsplit(a,3)
print(s)

