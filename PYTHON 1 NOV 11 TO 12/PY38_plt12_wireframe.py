import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

def f(fx,fy):
    return np.sin(np.sqrt(fx**2+fy**2))
    
x=np.linspace(-6,6,30)
y=np.linspace(-6,6,30)

x1,y1=np.meshgrid(x,y)
z1=f(x1,y1)

fig=plt.figure()
ax=plt.axes(projection='3d')

ax.plot_wireframe(x1,y1,z1, color='k')
ax.set_title("3D line plot")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
