import numpy as np
array=np.array([1,2,3,4,5,6,7,8])
print(f'acessing 2nd element:',array[2])
print(f'acessing 2nd to 5th element:',array[2:5])
array1=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(f'no. of dimension sof array1:',array.ndim)
print(f'accesing [4,5,6] in array1:',array1[0,1])