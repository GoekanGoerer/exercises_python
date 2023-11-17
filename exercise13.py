import numpy as np

M = np.array([3,1,2,4]).reshape(2, 2)

M_inv =  np.linalg.inv(M)
M_matmul1 = M_inv * M
M_matmul2 = np.matmul(M_inv, M)
#print(M_matmul2)
#test
print(np.matmul(M_matmul2, M))