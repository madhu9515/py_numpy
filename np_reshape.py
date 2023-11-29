import numpy as np
print(' convert  from 1D to 2D')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
print(' convert from 1D to 3D')
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr1 = arr1.reshape(2, 3, 2)
print(newarr1)