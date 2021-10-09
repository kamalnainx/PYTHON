##import numpy as np
##a=np.array([1,2,3,4,5])
##print(a)
##print(a[1])#2
##print(a[1:4])#all
##print(a[0:4:2])#skip one by one step
##print(a[-1])#2
##print(a[-1:-3:-1])#all
##print(a[-1:-4:-2])#skip one by one step





##import numpy as np
##a=np.array([1,2,3,4,5,6,7,8,9])
##print(a)
##x,y=a[0:3],a[4:7]
##print(x+y)
##
##y=0
##for x in a:     y+=x
##print(y)







##import numpy as np
##a=np.array([    [1,2,3,4,5,6,7,8,9] ,   [1,2,3,4,5,6,7,8,9] ])
##print(a)
##print(a[0,0:]+a[1,0:])
##print(a[0,3::-1])
##print(a[1,3:6])






##
##import numpy as np
##a=np.array([        [    [1,2,3,14,5,6,7,8,9] ,   [1,2,3,40,5,6,7,8,9] ]  ,   [    [1,2,3,44,5,6,7,8,9] ,   [1,2,3,"04",5,6,7,8,9] ]      ])
##print(a)
##print(a[0,0,3:6])#14,5,6
##print(a[0,1,3:6])#40,5,6
##print(a[1,0,1:4])#2,3,44
##print(a[1,1,1:4])#2,3,04


##print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")









##import numpy as np
##a=np.array([2,4,6,8,10])
##print(a)
##print(a.dtype)
##a=np.array([2,4,6.0,8,10])
##print(a)
##print(a.dtype)
##a=np.array([2,4,6.0,"8",10])
##print(a)
##print(a.dtype)








import numpy as np
a=np.array([2,4,6,8,10])
print(a)
print(a.dtype)
a=np.array([2,4,6,8,10], dtype='S')
print(a)
print(a.dtype)
a=np.array([2,4,6,8,10], dtype='i')
print(a)
print("i",a.dtype)
a=np.array([2,4,6,8,10], dtype='f')
print(a)
print("f",a.dtype)
a=np.array([2,4,6,8,10], dtype='S')
print(a)
print("s",a.dtype)
a=np.array([2,4,6,8,10], dtype='U')
print(a)
print("u",a.dtype)


a=np.array([2,4,6.0,8,10])
print(a)
print(a.dtype)
a=np.array([2,4,6.0,"8",10])
print(a)
print(a.dtype)



