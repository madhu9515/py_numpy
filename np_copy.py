import numpy as np
array=np.array([1,2,3,4,5])
array1=array.copy()
print(f'original array=',array)
print(f'copied array of array1=',array1)
print()
print('after modification of original array')
print()
array[1]=123456
print(f'original array=',array)
print(f'copied array of array1=',array1)
