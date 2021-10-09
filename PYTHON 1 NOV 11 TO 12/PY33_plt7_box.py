##import matplotlib.pyplot as plt
##import numpy as np
##
##b1=np.random.normal(100,10,200)
##fig=plt.figure()
##ax=fig.add_axes([.1,.1,.8,.8])
##ax.boxplot(b1)
##plt.show()








##import matplotlib.pyplot as plt
##import numpy as np
##
##b1=np.random.normal(100,10,200)
##b2=np.random.normal(100,10,200)
##b3=np.random.normal(100,10,200)
##b4=np.random.normal(100,10,200)
##bp=[b1,b2,b3,b4]
##fig=plt.figure()
##ax=fig.add_axes([.1,.1,.8,.8])
##ax.boxplot(bp)
##plt.show()







import matplotlib.pyplot as plt
import numpy as np

b1=np.random.normal(100,10,200)
b2=np.random.normal(80,20,200)
b3=np.random.normal(60,30,200)
b4=np.random.normal(40,40,200)
bp=[b1,b2,b3,b4]
fig=plt.figure()
ax=fig.add_axes([.1,.1,.8,.8])
ax.boxplot(bp)
plt.show()
