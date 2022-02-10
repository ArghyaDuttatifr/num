import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
z=np.loadtxt('data.txt.txt')
G=CubicSpline(z[:,0],z[:,1])
x=z[:,0]
y=[]
for k in range(len(x)):
    y.append(G(x[k]))
    fig,ax=plt.subplots(1,2)
    ax[0].scatter(z[:,0],z[:,1],)

    ax[0].set_title("Curve of Data Point")
    ax[1].plot(x,y)
    ax[1].set_title("Interpolation")
    plt.show()


def bisection(a,b,tol):
    r = (a+b)/2
    while(abs(G(r))>tol):
        if (G(r)*G(a)>0):
            a=r
        else :
            b =r                                                                                                
        r = 0.5*(a+b)
    return r
print("The root of the interpolated function found to be: ",bisection(-1,1,1e-9))
