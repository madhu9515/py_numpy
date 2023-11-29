import numpy as np
arr=np.array([6,16,8,9,10,15])
arr1=np.searchsorted(arr,16)
arr2=np.searchsorted(arr,7)
print('the value we want to find the index pos. is present in array list ')
print(arr1)
print('the value we want to find the index pos. is not present in array list,but we get index of that ')
print(arr2)

arrr = np.array([1, 3, 5, 7])

x = np.searchsorted(arrr, [2, 4, 6])
print('index pos. of [2,4,6 ] ijn above array list')
print(x)
