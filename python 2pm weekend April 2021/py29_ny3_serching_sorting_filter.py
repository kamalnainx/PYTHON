# arr=[1,2,3,4,5,6,7,8,76]
# findvalue=76
# for x in arr:
#     if x==findvalue:
#         print("yes, is this value in this list and value is",x)
    













# import numpy as np
# arr=np.array([1,9,2,3,4,9,5,6,7,8,76])
# findvalue=9
# v1=np.where(arr==findvalue)
# print(findvalue, " list index is :-",v1)















# import numpy as np
# arr=np.array([1,9,2,3,4,9,5,6,7,8,76])
# findvalue=0
# v1=np.where(arr%2==findvalue)
# print(findvalue, " list index is :-",v1)

























# import numpy as np
# arr=np.array([1,9,2,3,4,5,6,7,8,76])
# findvalue=9
# v1=np.searchsorted(arr,findvalue)
# print(findvalue, " list index is :-",v1)

























# import numpy as np
# arr=np.array([1,2,3,4,5])
# findvalue=2
# v1=np.searchsorted(arr,findvalue, side="left")
# print(findvalue, " list index is :-",v1)















# import numpy as np
# arr=np.array([1,3,5,7])
# x=np.searchsorted(arr,[3,5,7])
# print(x)


























# sort
# import numpy as np
# arr=np.array([1,9,3,7,5])
# print(np.sort(arr))
















# import numpy as np
# arr1=np.array([1,9,3,7,5])
# arr2=np.array(["banana","cherry","apple"])
# arr3=np.array([True, False, True, False])
# print(np.sort(arr1))
# print(np.sort(arr2))
# print(np.sort(arr3))























# import numpy as np
# arr1=np.array([[1,9,3,7,11,5],[1,9,11,3,7,5]])
# arr2=np.array([["banana","date","cherry","apple"],["banana","cherry","date","apple"]])
# print(np.sort(arr1))
# print(np.sort(arr2))















# import numpy as np
# arr1=np.array([[10,6,8,2,4],[1,9,3,7,5]])
# arr2=[]
# for x in arr1:
#     for y in x:
#        arr2.append(y) 
# sarr=np.sort(arr2)
# arr1=sarr.reshape(2,5)
# print(arr1)













































# filter
# import numpy as np
# arr=np.array([1,2,3,4,5,6])
# print(arr[[True,False,True,False,True,False]])
# print(arr[[False,True,False,True,False,True]])































# import numpy as np
# arr=np.array([1,2,3,4,5,6])
# sarr=[]
# for element in arr:
#     if element>3:
#         sarr.append(True)
#     else:
#         sarr.append(False)
# print(sarr)
# print(arr[sarr])






























# import numpy as np
# arr=np.array([1,2,3,4,5,6])
# sarr=[]
# for element in arr:
#     if element%2==0:
#         sarr.append(True)
#     else:
#         sarr.append(False)
# print(sarr)
# print(arr[sarr])




















# import numpy as np
# arr=np.array([1,2,3,4,5,6])
# sarr=[]
# for element in arr:
#     if element%2==1:
#         sarr.append(True)
#     else:
#         sarr.append(False)
# print(sarr)
# print(arr[sarr])
