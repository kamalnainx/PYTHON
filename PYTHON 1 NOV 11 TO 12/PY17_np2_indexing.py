##import numpy as np
##a=np.array([1,2,3,4,5])
##print(a)
##print(a[1])#2
##print(a[1:4])#all
##print(a[0:4:2])#skip one by one step
##




##import numpy as np
##a=np.array([1,2,3,4,5,6,7,8,9])
##print(a)
##print(a[0]+a[1])
##
##y=0
##for x in a:     y+=x
##print(y)







##import numpy as np
##a=np.array([    [1,2,3,4,5,6,7,8,9] ,   [1,2,3,4,5,6,7,8,9] ])
##print(a)
##print(a[0]+a[1])
##print(a[0,3])
##print(a[1,3:6])







import numpy as np
a=np.array([        [    [1,2,3,14,5,6,7,8,9] ,   [1,2,3,40,5,6,7,8,9] ]  ,   [    [1,2,3,44,5,6,7,8,9] ,   [1,2,3,"04",5,6,7,8,9] ]      ])
print(a)
print(a[0,0,3])#14
print(a[0,1,3])#40
print(a[1,0,3])#44
print(a[1,1,3])#04






