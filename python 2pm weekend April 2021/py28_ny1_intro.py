# pip install numpy



# import numpy

# arr=[1,2,3,4,5]
# print(arr,type(arr))
# arr=numpy.array([1,2,3,4,5])
# print(arr,type(arr))
# print(numpy.__version__)


















# import numpy as np
# arr=np.array((1,2,3,4,5))
# print(arr)

















# import numpy as np
# arr=np.array(   (   (1,2,3,4,5) ,   (1,2,3,4,5) )   )
# print(arr)

















# import numpy as np
# arr=np.array(   (      (   (1,2,3,4,5) ,   (1,2,3,4,5) )   ,   (   (1,2,3,4,5) ,   (1,2,3,4,5) )   ))
# print(arr)




























# import numpy as np
# arr1=np.array(1)
# arr2=np.array(  (1,2,3,4,5) )
# arr3=np.array(   (  (   (1,2,3,4,5) ,   (1,2,3,4,5) )   ))
# arr4=np.array(   (      (   (1,2,3,4,5) ,   (1,2,3,4,5) )   ,   (   (1,2,3,4,5) ,   (1,2,3,4,5) )   ))
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)
# print(arr4.ndim)




















# import numpy as np
# arr2=np.array(  (1,2,3,4,5) , ndmin=5)

# print(arr2,arr2.ndim)






# import numpy as np
# arr2=np.array(  [1,2,3,4,5] )

# print(arr2[0])
# print(arr2[1])
# print(arr2[2])
# print(arr2[3])























# import numpy as np
# arr2=np.array(  [  [1,2,3,4,5] , [11,22,33,44,55]   ]   )

# print(arr2[1,1])#22
# print(arr2[0,2])#3















# import numpy as np
# arr2=np.array(  [1,11,2,22,3,33,4,44,5,55] )

# print(arr2[0])
# print(arr2[1:5])
# print(arr2[3:])
# print(arr2[:3])
# print(arr2[-3:-1])
# print(arr2[1:7:2])
# print(arr2[::2])




















import numpy as np
arr2=np.array(  [  [0,1,21,2,31,3,41,4,51,5] , [10,11,20,22,30,33,40,44,50,55]   ]   )
print("222",arr2[1,0])
print(arr2[1,1:5])
print(arr2[1,3:])
print(arr2[1,:3])
print("226",arr2[0,-3:-1])
print(arr2[0,1:7:2])
print(arr2[0,::2])
print(arr2[0:1,:3])
print(arr2[:1,-3:-1])
print(arr2[0:,1:7:2])
print(arr2[::,::2])




