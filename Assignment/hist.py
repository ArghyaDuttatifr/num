import matplotlib.pyplot as plt
import numpy as np

mean, width = 0, 1.0
num = np.random.normal(mean , width, 1000)
plt.hist(num , bins =100 , facecolor = 'r', range=(-2.0,2.0))
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.title(" Histogram of 1000 numbers of Normal distribution")
plt.show()
