import numpy as np

arr = np.zeros((8, 8))

# print(arr)

arr[::2, ::2] = 1
arr[1::2, 1::2] = 1

# print(arr)

print(np.array([1, 0]*32).reshape(8, 8))






