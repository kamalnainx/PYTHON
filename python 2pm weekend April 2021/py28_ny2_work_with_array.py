# import numpy as z
# arr=z.array([   [1,3,5,7,9] ,   [2,4,6,8,10]    ])
# print(arr.shape)






# import numpy as np
# arr=np.array([   [1,3,5,7,9] ,   [2,4,6,8,10]    ], ndmin=4)
# print(arr.shape)
# print(arr)
















# import numpy as np
# arr=np.array([1,3,5,7,9,2,4,6,8,10])
# print(arr.shape)
# print(arr)
# arr2d=arr.reshape(2,5)
# print(arr2d.shape)
# print(arr2d)























# import numpy as np
# list1=[]
# for x in range(1,37):
#     list1.append(x)
# print(list1)    
# arr=np.array(list1)
# print(arr.shape)
# print(arr)
# arr4d=arr.reshape(3,2,3,2)#36=3*2*3*2
# print(arr4d.shape)
# print(arr4d)









# import numpy as np

# arr=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])
# print(arr.reshape(-1))
# print(arr)

























# import numpy as np

# arr=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])
# arr2d=arr.reshape(-1)
# print(arr2d)
# print(arr)

# for x in arr2d:
#     print(x)





















# import numpy as np

# arr=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])
# print(arr)

# for x in arr:#10    #2
#     for y in x:     #5
#         print(y)    #10     #10
































# import numpy as np

# arr=np.array([
#     [ [1,2,3,4,5],    [5,4,3,2,1]   ],
#     [ [1,2,3,4,5],    [5,4,3,2,1]   ],
#     [ [1,2,3,4,5],    [5,4,3,2,1]   ]
# ])
# print(arr)
# print()
# for x in arr:
#     print(x)





























# import numpy as np

# arr=np.array([
#     [ [1,2,3,4,5],    [5,4,3,2,1]   ],
#     [ [1,2,3,4,5],    [5,4,3,2,1]   ],
#     [ [1,2,3,4,5],    [5,4,3,2,1]   ]
# ])
# print(arr)
# print()
# for x in arr:
#     for y in x:
#         print(y)
#         # for z in y:
#         #     print(z)
#         print()
#     print("___________________")
























# import numpy as np

# arr1=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])
# arr2=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])
# arr3=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])

# print(arr1 , arr2, arr3)
# print("_____________________________________________")
# farr=np.concatenate((arr1,arr2))
# print(farr)






























# import numpy as np

# arr1=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])
# arr2=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])
# arr3=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])

# print(arr1 , arr2, arr3)
# print("_____________________________________________")
# farr=np.stack((arr1,arr2),axis=2)
# print(farr)






























# import numpy as np

# arr1=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])
# arr2=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])
# arr3=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])

# print(arr1 , arr2, arr3)
# print("_____________________________________________")
# farr=np.hstack((arr1,arr2))
# print(farr)




















# import numpy as np

# arr1=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])
# arr2=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])
# arr3=np.array([ [1,2,3,4,5],    [5,4,3,2,1]   ])

# print(arr1 , arr2, arr3)
# print("_____________________________________________")
# farr=np.vstack((arr1,arr2))
# print(farr)
# print("_____________________________________________")
# farr=np.dstack((arr1,arr2))
# print(farr)


















# import numpy as np

# arr1=np.array([1,2,3,4,5,5,4,3,2,1])

# print(arr1)
# print("_____________________________________________")
# sarr=np.array_split(arr1,2)
# print(sarr)





















# import numpy as np

# arr1=np.array([1,2,3,4,5,5,4,3,2,1])

# print(arr1)
# print("_____________________________________________")
# sarr=np.array_split(arr1,5)
# print(sarr)
# print(sarr[0])
# print(sarr[1])
# print(sarr[2])
# print(sarr[3])
# print(sarr[4])


















# import numpy as np

# arr1=np.array([1,2,3,4,5,5,4,3,2,1])

# print(arr1)
# print("_____________________________________________")
# sarr=np.array_split(arr1,5)
# print(sarr)

# for x in sarr:
#     print(x)


















# import numpy as np

# arr1=np.array([
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1]
    
# ])

# print(arr1)
# print("_____________________________________________")
# sarr=np.array_split(arr1,3)
# print(sarr)

# for x in sarr:
#     print(x,"\n")








# work
#vstack=vsplit
#sstack=dsplit
#hstack=hsplit

















# import numpy as np

# arr1=np.array([
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1],
#     [1,2,3,4,5,5,4,3,2,1]
    
# ])

# print(arr1)
# print("_____________________________________________")
# sarr=np.array_split(arr1,3, axis=1)
# print(sarr)

# for x in sarr:
#     print(x,"\n")
