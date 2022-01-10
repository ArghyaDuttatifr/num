def f(x):
    return (10 - x**2)
a= -2
b = 2
n = 1000

h =(b-a)/n
sum = 0.5* ( f(a) + f(b) )
for i in range(1, n-1 ):
    x= a + i*h
    sum = sum + f(x)
sum = h*sum
print( "value of integral = ", sum )
