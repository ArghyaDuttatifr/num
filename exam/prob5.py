import numpy as np
def f(x,y):
    return np.sqrt(4 - x**2 - y**2)
def midpoint_double2(f, a, b, c, d, nx, ny):
    def g(x):
        return midpoint(lambda y: f(x, y), c, d, ny)
    return midpoint(g, a, b, nx)
def midpoint_double1(f, a, b, c, d, nx, ny):
    hx = (b - a)/float(nx)
    hy = (d - c)/float(ny)
    I = 0
    for i in range(nx):
        for j in range(ny):
            xi = a + hx/2 + i*hx
            yj = c + hy/2 + j*hy
            I += hx*hy*f(xi, yj)
    return I
print ('The value of integral is = ' , midpoint_double1(f, -1, 1, -1, 1, 150, 150))
