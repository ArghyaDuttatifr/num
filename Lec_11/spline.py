import numpy as np
from scipy.interpolate import CubicSpline

x = np.array([0, 1, 2])
y = np.array([1, 2, 4])

cs = CubicSpline(x,y,bc_type='natural')


print('f(1.5) = ', cs(1.5))
print (" The actual value of 2^1.5 is: ", 2**1.5)
