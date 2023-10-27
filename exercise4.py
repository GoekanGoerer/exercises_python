# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:45:04 2023

@author: s_goerer20
"""

r = 0,5
a = 1
n = 10
s_n = []
cumulative_sum = 0

for k in range(0, n):
    cumulative_sum += a * r**((k))
    s_n.append(cumulative_sum)

s_n

print(s_n)
