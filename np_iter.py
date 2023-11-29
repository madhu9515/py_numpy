import numpy as np
array=np.array([1,2,3,4,5,6])
print('using for loop -- array')
for arr in array:
    print(arr,end=' ')

print('using for loop -- array1')
array1=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
for arr1 in array1:
    print(arr1)
print(' ')
print('using 2 for loops for getting each value in sub list')
for arr2 in array1:
    for arr4 in arr2:
        for arr6 in arr4:
            print(arr6,end=' ')

print(' ')
print('using nditer() attribute to array1 for get each value ')
for arr3 in np.nditer(array1): #np.nditer helps to get the each value present in the sub list
    print(arr3,end=' ')


