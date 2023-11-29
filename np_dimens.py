import numpy as np
#0D
Zero_D=np.array(234)
print(f'zero dimesional array:',Zero_D)
#1D
One_D=np.array([1,2,3,4])
print(f'one dimesional array:',One_D)
#2D
Two_D=np.array([[1,2,3],[4,5,6]])
print(f'Two dimesional array:',Two_D)
#3D
Three_D=np.array([[[1,2,3],[4,5,6]],[[4,5,6],[7,8,9]]])
print(f'Three dimesional array:',Three_D)
No_of_D=np.array([1,2,3,4],ndmin=5)
print(No_of_D)
print('finding no. of dimensions of above arrays')
print(One_D.ndim)
print(Two_D.ndim)
print(Three_D.ndim)
print(No_of_D.ndim)
