import numpy as np
x = np.array ([0, 1, 2 ]) 
y= np.array ([1, 2, 4 ]) 
m = len(x)
n = m-1
xp = 1.5
yp = 0

for i in range (n+1):
    p =1
    for j in range (n+1):
        if j != i:

            p *= (xp-x[j])/(x[i]-x[j])
    yp += y[i]*p
print ( ' for x = %.2f , y =%.f '% (xp,yp) )
