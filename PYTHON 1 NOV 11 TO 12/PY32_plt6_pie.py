##import matplotlib.pyplot as plt
##import numpy as np
##
##x=np.array([170,10,250,200,100,50])
##plt.pie(x)
##plt.show()







##import matplotlib.pyplot as plt
##import numpy as np
##
##x=np.array([170,10,250,200,100,50])
##ml=['a','b','c','d','e','f']
##plt.pie(x, labels=ml)
##plt.show()








##import matplotlib.pyplot as plt
##import numpy as np
##
##x=np.array([170,10,250,200,100,50])
##ml=['a','b','c','d','e','f']
##plt.pie(x, labels=ml, startangle=90)
##plt.show()







##
##import matplotlib.pyplot as plt
##import numpy as np
##
##x=np.array([170,10,250,200,100,50])
##ml=['a','b','c','d','e','f']
##mlout=[0,0,0,0,0,0]
##plt.pie(x, labels=ml, startangle=90,explode=mlout)
##plt.show()














##import matplotlib.pyplot as plt
##import numpy as np
##
##x       =  np.array(    [170, 10  ,250,200,  100  ,50])
##ml      =               ['a', 'b' ,'c','d',  'e'  ,'f']
##mlout   =               [0,   0.2 ,0,0,      0.4  ,0]
##plt.pie(x, labels=ml, startangle=90,explode=mlout)
##plt.show()












##import matplotlib.pyplot as plt
##import numpy as np
##
##x       =  np.array(    [170, 10  ,250,200,  100  ,50])
##ml      =               ['a', 'b' ,'c','d',  'e'  ,'f']
##mlout   =               [0,   0.2 ,0,0,      0.4  ,0]
##plt.pie(x, labels=ml, startangle=90,explode=mlout, shadow=True)
##plt.show()










##import matplotlib.pyplot as plt
##import numpy as np
##
##x       =  np.array(    [170, 10  ,250,200,  100  ,50])
##ml      =               ['a', 'b' ,'c','d',  'e'  ,'f']
##mlout   =               [0,   0.2 ,0,0,      0.4  ,0]
##mcolor  =               ["red","green","blue","hotpink","black","gray"]
##plt.pie(x, labels=ml, startangle=90,explode=mlout, shadow=True, colors=mcolor)
##plt.show()












##import matplotlib.pyplot as plt
##import numpy as np
##
##x       =  np.array(    [170, 10  ,250,200,  100  ,50])
##ml      =               ['a', 'b' ,'c','d',  'e'  ,'f']
##mlout   =               [0,   0.2 ,0,0,      0.4  ,0]
##mcolor  =               ["red","green","blue","hotpink","black","gray"]
##plt.pie(x, labels=ml, startangle=90,explode=mlout, shadow=True, colors=mcolor)
##plt.legend()
##plt.show()







import matplotlib.pyplot as plt
import numpy as np

x       =  np.array(    [170, 10  ,250,200,  100  ,50])
ml      =               ['a', 'b' ,'c','d',  'e'  ,'f']
mlout   =               [0,   0.2 ,0,0,      0.4  ,0]
mcolor  =               ["red","green","blue","hotpink","black","gray"]
plt.pie(x, labels=ml, startangle=90,explode=mlout, shadow=True, colors=mcolor)
plt.legend(title="list name")
plt.show()
