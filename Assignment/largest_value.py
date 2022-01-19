def largest( arr , n):
    max = arr[0]

    for i in range(1, n):
        if arr[i]>max:
            max = arr[i]
        return max
arr = [23, 45, 67, 13, 17, 19 , 25 ,20, 19, 33, 44]
n = len(arr)
value = largest( arr, n )
print (" largest value is : \n ", value )
