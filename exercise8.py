import numpy as np

A = np.eye(5, k=0)
B = A.copy()
B[3:,0:2] = 2
B[0:2,3:] = 3
print(B)