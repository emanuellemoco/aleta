# -*- Coding: UTF-8 -*-
#coding: utf-8

import math
import numpy as np
import matplotlib.pyplot as plt 


alpha = 0.0001  #m2/s
dX = 0.05       #m
dT = 5          #s


t_list = [0,20,20,20,20,20,20,20,20,20,0]
x = [0,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50]
#### 
beta=alpha*dT/(dX**2)
n = 0
aux = t_list[:]
while(n<104):

    for i in range(1,len(t_list)-1):
        
        aux[i] = t_list[i] + beta*(t_list[i+1]-2*t_list[i]+t_list[i-1])

    t_list = aux[:]
    n+=1

print(t_list)
plt.plot(x,t_list)
plt.grid()
plt.show()

