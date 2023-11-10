import math as mt
x = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]
log_x = [mt.log10(i) for i in x]
print(log_x)