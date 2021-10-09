# import matplotlib.pyplot as plt
# import numpy as np

# y=np.array([10,       1,      5,      3,      7])

# plt.pie(y)

# plt.show()









































# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array(["a",    "b",    "c",    "d",    "e"])
# y=np.array([10,       1,      5,      3,      7])

# plt.pie(y, labels=x)

# plt.show()









































# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array(["a",    "b",    "c",    "d",    "e"])
# y=np.array([10,       1,      5,      3,      7])

# plt.pie(y, labels=x, startangle=90)

# plt.show()









































# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array(["a",    "b",    "c",    "d",    "e"])
# y=np.array([10,       1,      5,      3,      7])
# myexplode= [0.2,      0,      0,      0,      0]

# plt.pie(y, labels=x, startangle=90, explode=myexplode)

# plt.show()








































# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array(["a",    "b",    "c",    "d",    "e"])
# y=np.array([10,       1,      5,      3,      7])
# myexplode= [0.2,      0,      0,      0,      0]

# plt.pie(y, labels=x, startangle=90, explode=myexplode, shadow="True")

# plt.show()








































# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array( ["a",    "b",    "c",    "d",    "e"])
# y=np.array( [10,       1,      5,      3,      7])
# myexplode=  [0.2,      0,      0,      0,      0]
# mycolor=    ["red","green","blue","pink","black"]
# plt.pie(y, labels=x, startangle=90, explode=myexplode, shadow="True", colors=mycolor)

# plt.show()









































# import matplotlib.pyplot as plt
# import numpy as np

# x=np.array( ["a",    "b",    "c",    "d",    "e"])
# y=np.array( [10,       1,      5,      3,      7])
# myexplode=  [0.2,      0,      0,      0,      0]
# mycolor=    ["red","green","blue","pink","black"]
# plt.pie(y, labels=x, startangle=90, explode=myexplode, shadow="True", colors=mycolor)
# plt.legend()
# plt.show()







































import matplotlib.pyplot as plt
import numpy as np

x=np.array( ["a",    "b",    "c",    "d",    "e"])
y=np.array( [10,       1,      5,      3,      7])
myexplode=  [0.2,      0,      0,      0,      0]
mycolor=    ["red","green","blue","pink","black"]
plt.pie(y, labels=x, startangle=90, explode=myexplode, shadow="True", colors=mycolor)
plt.legend(title="color values")
plt.show()








