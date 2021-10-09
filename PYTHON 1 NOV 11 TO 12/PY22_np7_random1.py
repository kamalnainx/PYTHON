##from numpy import random
##x=random.rand()
##print(x)
##x=random.randint(100)
##print(x)
##x=random.randint(100, size=(5))
##print(x)
##x=random.randint(100, size=(3,5))
##print(x)
##x=random.choice([5,10,20,40,80])
##print(x)
##x=random.choice([5,10,20,40,80],size=(3,5))
##print(x)
##print("----------------------------------------------------------------")
##y=random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(100))
##print(y)
##y=random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(3,5))
##print(y)









from numpy import random
import numpy as np

x=np.array([5,10,20,40,80])
print(x)
random.shuffle(x)
print(x)
print(random.permutation(x))

