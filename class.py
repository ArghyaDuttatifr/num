mport math 
def func(x):
    return x**2-10
def derivfunc(x):
    return 2*x
 x=0.1
for i in range (100):
x= x-func(x)/derivfunc(x)
print (x)
print (math.sqrt(10)
