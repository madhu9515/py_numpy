import numpy as np
array=np.array([1,2,3,4])
array1=array.view()
print(array)
print(array1)
print()
print('after changing the array ')
array[0]=45
print(f'original array=',array)
print(f'view of the original array=',array1)