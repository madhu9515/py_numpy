import numpy as np
array=np.array([1,2,3,4,5,6])
array1=np.array([[1,2,3],[4,5,6]])
print(f'shape of an array',array.shape)
print(f'shape of an array1=',array1.shape)
array3 = np.array([1, 2, 3, 4], ndmin=5)

print(array3)
print('shape of array3 :', array3.shape)