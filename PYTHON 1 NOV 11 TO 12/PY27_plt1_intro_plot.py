##import matplotlib
##print(matplotlib.__version__)


##
##import matplotlib.pyplot

##matplotlib.pyplot.plot(     [1,2,3,4,5],
##                            [1,5,2,4,3])
##matplotlib.pyplot.show()




##import matplotlib.pyplot as plt
##plt.plot([1,2,3,4,5],
##         [1,5,2,4,3])
##plt.show()






##import matplotlib.pyplot as plt
##x=[1,2,3,4,5]
##y=[1,5,2,4,3]
##plt.plot(x,y)
##plt.show()









##import matplotlib.pyplot as plt
##import numpy as np
##x=np.array([1,2,3,4,5])
##y=np.array([1,5,2,4,3])
##plt.plot(x,y)
##plt.show()










##import matplotlib.pyplot as plt
##import pandas as pd
##x=pd.Series([1,2,3,4,5])
##y=pd.Series([1,5,2,4,3])
##plt.plot(x,y)
##plt.show()















##import matplotlib.pyplot as plt
##import numpy as np
##x=np.array([1,2,3,4,5])
##y=np.array([1,5,2,4,3])
##plt.plot(x,y,"o")
##plt.show()









##import matplotlib.pyplot as plt
##import numpy as np
##y=np.array([1,5,2,4,3])
##plt.plot(y,"o")
##plt.show()









##import matplotlib.pyplot as plt
##import numpy as np
##y=np.array([1,10,2,9,3,8,4,7,5])
##plt.plot(y)
##plt.show()










##import matplotlib.pyplot as plt
##import numpy as np
##y=np.array([1,10,2,9,3,8,4,7,5])
##plt.plot(y, marker="o")
##plt.show()












##
##import matplotlib.pyplot as plt
##import numpy as np
##y=np.array([1,10,2,9,3,8,4,7,5])
##plt.plot(y, "H-.r",linewidth="5.5", color='#00f' , ms=20, mec='#000', mfc='#fff')
####line style =              -, --, :, -.
####line width =              linewidth=float/int
####marker style =            o,*, ., , x, X, +, P, s, D, d, p, H, h, ^, |, _
####color style =             r, g, b, c, m, y, k, w
####marker size =             ms= int
####marker edge color=        mec=color code
####marker face color=        mfc=color code
##plt.show()









##import matplotlib.pyplot as plt
##import numpy as np
##y=np.array([1,10,2,9,3,8,4,7,5])
##plt.plot(y, linestyle="dotted" ,c='#0f0', linewidth="5", marker="o", ms=20, mec='#000', mfc='#ff0')
##
##plt.show()
