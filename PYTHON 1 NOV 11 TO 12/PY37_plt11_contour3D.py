##import matplotlib.pyplot as plt
##import numpy as np
##from mpl_toolkits import mplot3d
##
##def f(fx,fy):
##    return np.sin(np.sqrt(fx**2+fy**2))
##    
##x=np.linspace(-6,6,36)
##y=np.linspace(-6,6,36)
##x1,y1=np.meshgrid(x,y)
##z1=f(x1,y1)
##
##fig=plt.figure()
##ax=plt.axes(projection='3d')
##
##ax.contour3D(x1,y1,z1,50)
##ax.set_title("3D line plot")
##plt.show()









##import matplotlib.pyplot as plt
##import numpy as np
##from mpl_toolkits import mplot3d
##
##def f(fx,fy):
##    return np.sin(np.sqrt(fx**2+fy**2))
##    
##x=np.linspace(-6,6,36)
##y=np.linspace(-6,6,36)
##x1,y1=np.meshgrid(x,y)
##z1=f(x1,y1)
##
##fig=plt.figure()
##ax=plt.axes(projection='3d')
##
##ax.contour3D(x1,y1,z1,50, cmap='binary')
##ax.set_title("3D line plot")
##plt.show()









import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

def f(fx,fy):
    return np.sin(np.sqrt(fx**2+fy**2))
    
x=np.linspace(-6,6,36)
y=np.linspace(-6,6,36)
x1,y1=np.meshgrid(x,y)
z1=f(x1,y1)

fig=plt.figure()
ax=plt.axes(projection='3d')

ax.contour3D(x1,y1,z1,50, cmap='binary')
ax.set_title("3D line plot")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
