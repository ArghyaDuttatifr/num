list= [10, 20, 26, 29 , 35, 47, 77, 61, 19, 55, 81, 43, 44]
n = int(input ( " n largest elements, n =  "))

list.sort()
value = list[-n:]
print ( n,' largest values are : \n ', value )

