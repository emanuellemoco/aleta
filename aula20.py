# -*- Coding: UTF-8 -*-
#coding: utf-8

import math
import numpy as np
import matplotlib.pyplot as plt 

alpha = 0.25  #m2/s
dX = 0.1
dY = 0.1     #m
dT = 0.01    #s

k = 0.23      # W/m.℃ Condutividade térmica:
cp = 897         # J/kg.℃ Calor específico:  
ro = 2.7e-6   # kg/m³Densidade:
alpha = k/(ro*cp) #difusividade (depende da condutividade, ro e calor especifico)


print(alpha)
# t_list = [0,20,20,20,20,20,20,20,20,20,0]
# x = [0,0.1,0.2,0.3,0.4,0.5]

tol = 1e-4


def getTemp(m,nn,alpha,dT,dX,dY,tol,t):
    beta = alpha*dT
    n = 0
    T = np.zeros( (5, 5) )
    T_f = np.copy(T)
    for j in range(m):
        T[0][j] = 150
        T[j][-1] = 50   
    
    print(T)

    while(n<(t/dT )):
        for i in range(1,m-1):
            for j in range(nn-1):
                if j ==0:
                    T[i][j] = (alpha * dT) * ( T_f[i+1][0] + T_f[i-1][0] + 2*T_f[i][j+1]) + (1 - 4 * alpha * dT) * T_f[i][0]
                else:
                    partX = (T_f[i][j+1] - 2*T_f[i][j] + T_f[i][j-1])/(dX**2)

                    partY = (T_f[i+1][j] - 2*T_f[i][j] + T_f[i-1][j])/(dY**2)

                    T[i][j] =  T_f[i][j] + beta * (partX + partY)
               #if (T[i][j]-T_f[i][j])/T[i][j]<1e-4:
                    #print("Saiu pela tolerancia")
                    #print("Retornou depois de: ",n*dT," segundos")

                    #return T_f
        
        T_f = np.copy(T)
        n+=1    
    print("Retornou depois de: ",n*dT," segundos")
    return T_f



results = getTemp(5,5,alpha,dT,dX,dY,tol,1)

print(results[2][2])

plt.imshow(results, cmap='Reds', interpolation='nearest')
plt.colorbar()
plt.show()

