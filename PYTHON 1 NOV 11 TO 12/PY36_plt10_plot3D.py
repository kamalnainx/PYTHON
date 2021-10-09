##import matplotlib.pyplot as plt
##import numpy as np
##from mpl_toolkits import mplot3d
##
##z=np.linspace(0,1,200)
##x=z*np.sin(20*z)
##y=z*np.cos(20*z)
##
##fig=plt.figure()
##ax=plt.axes(projection='3d')
##
##ax.plot3D(x,y,z)
##
##plt.show()





##import matplotlib.pyplot as plt
##import numpy as np
##from mpl_toolkits import mplot3d
##
##z=np.linspace(0,1,100)
##x=z*np.sin(20*z)
##y=z*np.cos(20*z)
##
##fig=plt.figure()
##ax=plt.axes(projection='3d')
##
##ax.plot3D(x,y,z,'gray')
##ax.set_title("3D line plot")
##plt.show()
##









import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

z=np.linspace(0,1,100)
x=z*np.sin(20*z)
y=z*np.cos(20*z)
xy=x+y
fig=plt.figure()
ax=plt.axes(projection='3d')

ax.scatter(x,y,z,c=xy)
ax.set_title("3D line plot")
plt.show()

