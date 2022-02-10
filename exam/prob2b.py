mport numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x1= []
y1= []
for i in range (1 , 51 ):
    if i%5==0:
        x1.append(i)
        y1.append(np.pi*i*i)    #as area = np.pi * r**2
plt.plot(x1, y1, label="change of area with radius")
plt.legend()
plt.xlabel("Radius")
plt.ylabel("Area")
plt.title('Area changes with Radius')
plt.show()

from scipy import interpolate
cs = CubicSpline(x1, y1 ,bc_type='natural')
plt.annotate ( "point x = 13 or radius r = 13 ", (13, cs(13)))
plt.show()
print('f(13) = ', cs(13))
