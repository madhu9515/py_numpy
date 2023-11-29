import numpy as np
array=np.array([1,2,3,4,5])
print(f'data typoe of  array:',array.dtype)
array1=np.array([1,2,3,4,5],dtype='S')
print(f'convert to string:',array1)
array2=np.array([1.2,2.3,4.5])
print(array2.dtype)
print()
print('covert one float to another integer')
array3=np.array([1.2,2.3,4.5])
print(array3.astype(int))

