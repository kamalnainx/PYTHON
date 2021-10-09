##import matplotlib.pyplot as plt
##import numpy as np
##xlist=np.linspace(-3.0,3.0,100)
##ylist=np.linspace(-3.0,3.0,100)
##x,y=np.meshgrid(xlist,ylist)
##z=np.sqrt(x**2+y**2)
##
##fig,ax=plt.subplots(1,1)
##
##ax.contourf(x,y,z)
##plt.show()









import matplotlib.pyplot as plt
import numpy as np
xlist=np.linspace(-3.0,3.0,100)
ylist=np.linspace(-3.0,3.0,100)
x,y=np.meshgrid(xlist,ylist)
z=np.sqrt(x**2+y**2)
fig,ax=plt.subplots(1,1)
cb1=ax.contourf(x,y,z)
fig.colorbar(cb1)
plt.show()
