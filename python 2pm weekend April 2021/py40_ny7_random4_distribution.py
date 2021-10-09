#binomical sistribution
# n = number 
# p = probability
# size= shape





# from numpy import random
# x=random.binomial(n=10, p=.5, size=10)
# print(x)

















# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# x=random.binomial(n=10, p=.5, size=10)
# sns.distplot(x)

# print(x)
# plt.show()





















# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# x=random.binomial(n=10, p=.5, size=10)
# # sns.distplot(x)
# sns.distplot(x, kde=False)

# print(x)
# plt.show()






























# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# x=random.binomial(n=10, p=.5, size=10)
# # sns.distplot(x)
# # sns.distplot(x, kde=False)
# # sns.distplot(x, kde=False, hist=False)
# sns.distplot(x, kde=False, hist=True)


# print(x)
# plt.show()





































# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# nx=random.normal(loc=50, scale=5, size=100)
# bx=random.binomial(n=100, p=.5, size=100)
# # sns.distplot(x)
# # sns.distplot(x, kde=False)
# # sns.distplot(x, kde=False, hist=False)
# sns.distplot(nx, kde=True, hist=False)
# sns.distplot(bx, kde=True, hist=False)



# plt.show()



































# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# nx=random.normal(loc=50, scale=5, size=100)
# bx=random.binomial(n=100, p=.5, size=100)

# # sns.distplot(nx, kde=True, hist=False)
# # sns.distplot(bx, kde=True, hist=False)
# sns.distplot(nx, kde=True, hist=False, label="normal")
# sns.distplot(bx, kde=True, hist=False, label="bunomial")


# plt.legend()
# plt.show()



































# poisson distribution
# lam= rate of numbers occurences
# size=shape size(array)


# from numpy import random

# x=random.poisson(lam=3, size=10)

# print(x)








































# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# # nx=random.normal(loc=50, scale=5, size=100)
# # bx=random.binomial(n=100, p=.5, size=100)
# rpx=random.poisson(lam=5, size=100)

# # sns.distplot(nx, kde=True, hist=False)
# # sns.distplot(bx, kde=True, hist=False)
# # sns.distplot(nx, kde=True, hist=False, label="normal")
# # sns.distplot(bx, kde=True, hist=False, label="bunomial")
# sns.distplot(rpx, kde=True, hist=True, label="poisson")


# plt.legend()
# plt.show()

































# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# nx=random.normal(loc=50, scale=5, size=100)
# bx=random.binomial(n=100, p=.5, size=100)
# rpx=random.poisson(lam=50, size=100)

# sns.distplot(nx, kde=True, hist=False, label="normal")
# sns.distplot(bx, kde=True, hist=False, label="bunomial")
# sns.distplot(rpx, kde=True, hist=False, label="poisson")


# plt.legend()
# plt.show()



































# uniform distribution
# a = lower bound
# b = upper bound
# size=shape of array

# import numpy.random as ran

# x=ran.uniform(size=(2,3))

# print(x)








































# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# # nx=random.normal(loc=50, scale=5, size=100)
# # bx=random.binomial(n=100, p=.5, size=100)
# # rpx=random.poisson(lam=5, size=100)
# rux=random.uniform(size=100)

# # sns.distplot(nx, kde=True, hist=False)
# # sns.distplot(bx, kde=True, hist=False)
# # sns.distplot(nx, kde=True, hist=False, label="normal")
# # sns.distplot(bx, kde=True, hist=False, label="bunomial")
# # sns.distplot(rpx, kde=True, hist=True, label="poisson")
# sns.distplot(rux, kde=True, hist=True, label="uniform")


# plt.legend()
# plt.show()































# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# nx=random.normal(loc=50, scale=5, size=100)
# bx=random.binomial(n=100, p=.5, size=100)
# rpx=random.poisson(lam=5, size=100)
# rux=random.uniform(size=10)

# sns.distplot(nx, kde=True, hist=False, label="normal")
# sns.distplot(bx, kde=True, hist=False, label="bunomial")
# sns.distplot(rpx, kde=True, hist=False, label="poisson")
# sns.distplot(rux, kde=True, hist=False, label="uniform")


# plt.legend()
# plt.show()

































# logistic distributions
# loc =   mean
# scale=  standard deviation
# size=   shape of array






# import numpy.random as ran

# x=ran.logistic(loc=1, scale=2, size=(3,4))

# print(x)




































# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# rux=random.logistic(size=100)

# sns.distplot(rux, kde=True, hist=False, label="logistic")


# plt.legend()
# plt.show()







































# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# ldssx=random.logistic(scale=5, size=100)
# ldsx=random.logistic(size=100)

# sns.distplot(ldssx, kde=True, hist=True, label="logistic scale size")
# sns.distplot(ldsx, kde=True, hist=False, label="logistic size")


# plt.legend()
# plt.show()





































# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# nx=random.normal(loc=50, scale=5, size=100)
# bx=random.binomial(n=100, p=.5, size=100)
# rpx=random.poisson(lam=5, size=100)
# # rux=random.uniform(size=2)
# rlsx=random.logistic(size=10)
# rlssx=random.logistic(scale=5, size=100)


# sns.distplot(nx, kde=True, hist=False, label="normal")
# sns.distplot(bx, kde=True, hist=False, label="bunomial")
# sns.distplot(rpx, kde=True, hist=False, label="poisson")
# # sns.distplot(rux, kde=True, hist=False, label="uniform")
# sns.distplot(rlsx, kde=True, hist=False, label="logistic size")
# sns.distplot(rlssx, kde=True, hist=False, label="logistic scale size")


# plt.legend()
# plt.show()



























# multinomial distribution
# n       = number of possible outcomes
# pvals   = probabilites of outcomes
# size    = shapes od array






# import numpy.random as ran

# x=ran.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6])

# print(x)



































# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# nx=random.normal(loc=50, scale=5, size=100)
# bx=random.binomial(n=100, p=.5, size=100)
# rpx=random.poisson(lam=5, size=100)
# # rux=random.uniform(size=2)
# rlsx=random.logistic(size=10)
# rlssx=random.logistic(scale=5, size=100)
# rmdx=random.multinomial(n=10, pvals=[2/10,2/10,2/10,2/10,2/10])

# sns.distplot(nx, kde=True, hist=False, label="normal")
# sns.distplot(bx, kde=True, hist=False, label="bunomial")
# sns.distplot(rpx, kde=True, hist=False, label="poisson")
# # sns.distplot(rux, kde=True, hist=False, label="uniform")
# sns.distplot(rlsx, kde=True, hist=False, label="logistic size")
# sns.distplot(rlssx, kde=True, hist=False, label="logistic scale size")
# sns.distplot(rmdx, kde=True, hist=False, label="multinomial")

# plt.legend()
# plt.show()




























# exponential distrinution
# scale = poisson distributions
# size  = shape of array


# from matplotlib import scale
# import numpy.random as ran

# x=ran.exponential(scale=2, size=(3,5))

# print(x)








































# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# # nx=random.normal(loc=50, scale=5, size=100)
# # bx=random.binomial(n=100, p=.5, size=100)
# # rpx=random.poisson(lam=5, size=100)
# # # rux=random.uniform(size=2)
# # rlsx=random.logistic(size=10)
# # rlssx=random.logistic(scale=5, size=100)
# # rmdx=random.multinomial(n=10, pvals=[2/10,2/10,2/10,2/10,2/10])
# resx=random.exponential(size=100)

# # sns.distplot(nx, kde=True, hist=False, label="normal")
# # sns.distplot(bx, kde=True, hist=False, label="bunomial")
# # sns.distplot(rpx, kde=True, hist=False, label="poisson")
# # # sns.distplot(rux, kde=True, hist=False, label="uniform")
# # sns.distplot(rlsx, kde=True, hist=False, label="logistic size")
# # sns.distplot(rlssx, kde=True, hist=False, label="logistic scale size")
# # sns.distplot(rmdx, kde=True, hist=False, label="multinomial")
# sns.distplot(resx, kde=True, hist=False, label="exponential")

# plt.legend()
# plt.show()

























# from numpy import random
# import seaborn as sns
# import matplotlib.pyplot as plt

# nx=random.normal(loc=50, scale=5, size=100)
# bx=random.binomial(n=100, p=.5, size=100)
# rpx=random.poisson(lam=5, size=100)
# # rux=random.uniform(size=2)
# rlsx=random.logistic(size=10)
# rlssx=random.logistic(scale=5, size=100)
# rmdx=random.multinomial(n=10, pvals=[2/10,2/10,2/10,2/10,2/10])
# resx=random.exponential(size=100)

# sns.distplot(nx, kde=True, hist=False, label="normal")
# sns.distplot(bx, kde=True, hist=False, label="bunomial")
# sns.distplot(rpx, kde=True, hist=False, label="poisson")
# # sns.distplot(rux, kde=True, hist=False, label="uniform")
# sns.distplot(rlsx, kde=True, hist=False, label="logistic size")
# sns.distplot(rlssx, kde=True, hist=False, label="logistic scale size")
# sns.distplot(rmdx, kde=True, hist=False, label="multinomial")
# sns.distplot(resx, kde=True, hist=False, label="exponential")

# plt.legend()
# plt.show()


























from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

nx=random.normal(loc=50, scale=5, size=100)
bx=random.binomial(n=100, p=.5, size=100)
rpx=random.poisson(lam=5, size=100)
# rux=random.uniform(size=2)
rlsx=random.logistic(size=10)
rlssx=random.logistic(scale=5, size=100)
rmdx=random.multinomial(n=10, pvals=[2/10,2/10,2/10,2/10,2/10])
resx=random.exponential(size=1000)

sns.distplot(nx, kde=True, hist=False, label="normal")
sns.distplot(bx, kde=True, hist=False, label="bunomial")
sns.distplot(rpx, kde=True, hist=False, label="poisson")
# sns.distplot(rux, kde=True, hist=False, label="uniform")
sns.distplot(rlsx, kde=True, hist=False, label="logistic size")
sns.distplot(rlssx, kde=True, hist=False, label="logistic scale size")
sns.distplot(rmdx, kde=True, hist=False, label="multinomial")
sns.distplot(resx, kde=True, hist=False, label="exponential")

plt.legend()
plt.show()









