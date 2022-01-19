import matplotlib.pyplot as plt
import numpy as np
mean =0
width =1.0
x=np.random.normal(mean, width ,1000)
y=np.random.rand(1000)
plt.subplot(1,2,1)
plt.hist(x, bins = 100,range=(-2.0,2.0), density=True)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Histogram of 1000 normally distributed Random Numbers", size ='8')

plt.subplot(1,2,2)
plt.hist(y, 100, density=True)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Histogram of 1000 Random Numbers", size = '8')

plt.suptitle("Histogram using Pyplot")
plt.show()
