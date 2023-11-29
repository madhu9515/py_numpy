import numpy as np
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()
print("if array owns the data it will return 'NONE'")
print("if array doesn't owns data it will return original object")

print(f'copy object owns the data=',x.base)
print(f'view doesnt owns the data=',y.base)