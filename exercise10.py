import numpy as np

E = np.array([[[1,2,3], [4,5,6], [7,8,9]], [[9,8,7], [6,5,4], [3,2,1]], [[9,8,7], [3,2,1], [6,5,4]]])

print(E.ndim)
print(E.shape)
print(E)

print(E.sum(axis=0))