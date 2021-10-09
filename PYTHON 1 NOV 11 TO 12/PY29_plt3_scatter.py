##import matplotlib.pyplot as plt
##import numpy as np
##
##
##px1=np.array([0,10,12,3,4])
##py1=np.array([0,1,2,13,40])
##plt.scatter(px1,py1)
##plt.title("sales")
##plt.show()







##import matplotlib.pyplot as plt
##import numpy as np
##
##
##px1=np.array([0,10,12,3,4])
##py1=np.array([1,1,2,13,40])
##plt.scatter(px1,py1, color='r')
##
##px1=np.array([0,10,12,33,4,15])
##py1=np.array([0,1,22,13,40,35])
##plt.scatter(px1,py1, color="#00ff00")
##
##plt.title("sales")
##plt.show()







##
##import matplotlib.pyplot as plt
##import numpy as np
##
##
##px1=np.array([0,10,12,3,4])
##py1=np.array([1,1,2,13,40])
##plt.scatter(px1,py1, color='r')
##
##px1=np.array([0,10,12,33,4,15])
##py1=np.array([0,1,22,13,40,35])
##colors=np.array(['red','green','blue','yellow','pink','orange'])
##plt.scatter(px1,py1, color=colors)
##
##plt.title("sales")
##plt.show()











##import matplotlib.pyplot as plt
##import numpy as np
##
##
##px1=np.array([0,10,12,3,4])
##py1=np.array([1,1,2,13,40])
##plt.scatter(px1,py1, color='r')
##
##px1=np.array([0,10,12,33,4,15])
##py1=np.array([0,1,22,13,40,35])
##colors=np.array(['red','green','blue','yellow','pink','orange'])
##plt.scatter(px1,py1, color=colors,cmap='viridis')
##plt.colorbar()
##
##plt.title("sales")
##plt.show()















##import matplotlib.pyplot as plt
##import numpy as np
##
##px1=np.random.randint(100,size=(100))
##py1=np.random.randint(100,size=(100))
##colors=np.random.randint(100,size=(100))
##plt.scatter(px1,py1, c=colors,cmap='Blues')
##plt.colorbar()
##
##plt.title("sales")
##plt.show()







##import matplotlib.pyplot as plt
##import numpy as np
##
##px1=np.random.randint(100,size=(100))
##py1=np.random.randint(100,size=(100))
##colors=np.random.randint(100,size=(100))
####plt.scatter(px1,py1, c=colors,cmap='cool')
##plt.scatter(px1,py1, c=colors,cmap='flag')
##plt.colorbar()
##plt.title("sales")
##plt.show()











##
##import matplotlib.pyplot as plt
##import numpy as np
##
##px1=np.random.randint(100,size=(100))
##py1=np.random.randint(100,size=(100))
##colors=np.random.randint(100,size=(100))
##size1=np.random.randint(100,size=(100))
####plt.scatter(px1,py1, c=colors,cmap='cool')
##plt.scatter(px1,py1, c=colors,cmap='flag', s=size1)
##plt.colorbar()
##plt.title("sales")
##plt.show()











import matplotlib.pyplot as plt
import numpy as np

px1=np.random.randint(100,size=(100))
py1=np.random.randint(100,size=(100))
colors=np.random.randint(100,size=(100))
size1=2*np.random.randint(1000,size=(100))

plt.scatter(px1,py1, c=colors,cmap='flag', s=size1, alpha=0.5)
plt.colorbar()
plt.title("sales")
plt.show()
