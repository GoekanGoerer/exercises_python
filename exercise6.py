# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:34:34 2023

@author: s_goerer20
"""

x = "Hello, Berlin!"

x_list = list(x)

count_letters = []

for buchstabe in x_list:
    count_letters.append(buchstabe.isalpha())
    
print(sum(count_letters))