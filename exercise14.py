import numpy as np

import math as mt

y = [2, 3, 8, 4, 10, 1, 9, 5, 1, 0]

std = np.std(y)
print(std)
#std_abw = mt.sqrt((1/len(y)*(np.sum(y) - np.mean(y))^2))
#print(std_abw)