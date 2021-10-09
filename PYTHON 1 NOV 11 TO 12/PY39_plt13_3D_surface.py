import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

x=np.outer(np.linspace(-2,2,30),np.ones(30))
y=x.copy().T #t=transpose
z=np.cos(x**2+y**2)

fig=plt.figure()
ax=plt.axes(projection='3d')

ax.plot_surface(x,y,z, cmap='viridis', edgecolor='none')
ax.set_title("3D surface plot")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
