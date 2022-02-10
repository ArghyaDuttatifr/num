import numpy as np
def f(x):
    return np.sqrt(100-x*x)
a= -10
b = 10
n = 200
s = 0.5 * ( f(a) + f(b) )
h =(b-a)/n
xo = np.arange (a+h , b , 2*h) 
xe = np.arange (a+2*h , b , 2*h)  
value = h/3 *( f(a) + 4* sum( f(xo)) + 2* sum( f(xe)) + f(b) )
A = 2*value
print( "The value of the area is = ",A )
print (' The actual value is ', np.pi * 100)
