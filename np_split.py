import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print(newarr)
newarr1=np.array_split(arr,2)
print(newarr1)
