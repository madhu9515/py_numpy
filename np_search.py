import numpy as np


arrr=np.array([1,2,1,3,4,1,5,1])
arrr1=np.where(arrr==1)
print('print the indexes of element contaning 1 ')
print(arrr1)

arr=np.array([1,2,3,4,5,6,7,8])
arr1=np.where(arr==4)
arr2=np.where(arr%2==0)
print('print index position of value 4')
print(arr1)
print('print the values divisible by 2')
print(arr2)

