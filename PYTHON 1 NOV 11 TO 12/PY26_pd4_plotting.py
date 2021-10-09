##import pandas as pd
##import matplotlib.pyplot as plt
##
##df=pd.read_csv('file/sdf.csv')
##df.plot()
##plt.show()










import pandas as pd
import matplotlib.pyplot as plt

import sys
import matplotlib
matplotlib.use('Agg')

df=pd.read_csv('file/sdf.csv')
df.plot()
plt.show()

plt.savefig(StdOutputFile.buffer)
sys.stdout.flush()
