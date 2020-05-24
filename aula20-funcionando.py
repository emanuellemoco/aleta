# -*- Coding: UTF-8 -*-
#coding: utf-8

import math
import numpy as np
import matplotlib.pyplot as plt 

dX = 0.1
dY = 0.1    #m
dT = 0.001    #s

k = 0.23e3      # W/m.℃ Condutividade térmica:
cp = 897         # J/kg.℃ Calor específico:  
ro = 2.7e3   # kg/m³Densidade:
alpha = k/(ro*cp) #difusividade (depende da condutividade, ro e calor especifico)

""" 
0.04
0.08
0.12
0.16
0.20
0.24
0.28
0.32
0.36
0.40
 """
 
# t_list = [0,20,20,20,20,20,20,20,20,20,0]
# x = [0,0.1,0.2,0.3,0.4,0.5]

tol = 1e-4

def getTemp(m,nn,alpha,dT,dX,dY,tol,t):
    beta = alpha * dT
    f_zero = alpha*dT/(dX**2)
    n = 0
    T = np.zeros( (m, nn) )
    for j in range(m):
        T[0][j] = 150
        T[j][-1] = 50 
    T_f = np.copy(T)


    while(n<(t/dT)):
        lista_erros = []        
        for i in range(1,m-1):
            for j in range(nn-1):
                
                if j == 0:
                    #print(150*f_zero)
                    T[i][j] = (f_zero) * ( 2*T_f[i][1] + T_f[i+1][0] + T_f[i-1][0]) + (1 - 4 * f_zero)* T_f[i][0]
                
                else:
                    partX = (T_f[i][j+1] - 2*T_f[i][j] + T_f[i][j-1])/(dX**2)

                    partY = (T_f[i+1][j] - 2*T_f[i][j] + T_f[i-1][j])/(dY**2)

                    T[i][j] =  T_f[i][j] + beta * (partX + partY)
                
                if (T[i][j]!= 0):
                    erro = np.abs((T[i][j]-T_f[i][j])/T[i][j])
                    lista_erros.append(erro)
        
        if(np.max(lista_erros)<1e-8):
            print("Convergiu após {0} segundos".format(n*dT) )
            return T
        
            
        
        
        T_f = np.copy(T)
        n+=1    
    print("Retornou depois de: ",n*dT," segundos")
    print("Erro relativo máximo: ", np.max(lista_erros))
    return T_f



results = getTemp(5,5,alpha,dT,dX,dY,tol,10)


#for i in range(len(results)):
 #   print(results[i][0])


print(results.round(2))

plt.imshow(results, cmap='Reds', interpolation='nearest')
plt.colorbar()
plt.show()