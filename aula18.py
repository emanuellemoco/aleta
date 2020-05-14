# -*- Coding: UTF-8 -*-
#coding: utf-8

import math
import numpy as np
import matplotlib.pyplot as plt 


alpha = 1 #cm2/s
dT = 5
dX = 5

t_list = [0,20,20,20,20,20,20,20,20,20,0]
x = [0,5,10,15,20,25,30,35,40,45,50]
#### 

n = 0
while(n<104):
    for i in range(len(t_list)):
        if i ==0:
            t = 0
        elif (i==(len(t_list)-1)):
            t  = 0
        else:
            t =t_list[i] + alpha*dT/(dX**2)*(t_list[i+1]-2*t_list[i]+t_list[i-1])


        t_list[i] = t
        
    n+=1


plt.plot(x,t_list)
plt.grid()
plt.show()

