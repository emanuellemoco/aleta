# -*- Coding: UTF-8 -*-
#coding: utf-8
import math
import matplotlib.pyplot as plt 
import numpy as np


def burger(m,n,T,t,dT,dX,dY, alpha, Q, K):
    count = 0  
    C = np.zeros((m,n))   

    C_temp = np.copy(C)

    while(count<t/dT):
        for i in range(1,m-1):
            for j in range(1,n-1):
                if (count*dT<=T) and np.abs(i*dY-b)<0.0001 and np.abs(i*dX-a)<0.0001:
                    v = alpha * math.sin(math.pi*j*dX/5)
                    C[i][j] = C_temp[i][j] -  dT*(alpha*(C_temp[i][j+1]-C_temp[i][j-1])/dX + v[i][j]*(C_temp[i-1][j]-C_temp[i+1][j])/dY - K * (C_temp[i][j-1]-2*C_temp[i][j]+C_temp[i][j+1])/dX**2 - K * (C_temp[i-1][j]-2*C_temp[i][j]+C_temp[i+1][j])/dY**2 - Q/(dX*dY)) 
                else:
                    v = alpha * math.sin(math.pi*j*dX/5)
                    C[i][j] = C_temp[i][j] - dT*(alpha*(C_temp[i][j+1]-C_temp[i][j-1])/dX + v*(C_temp[i-1][j]-C_temp[i+1][j])/dY - K * (C_temp[i][j-1]-2*C_temp[i][j]+C_temp[i][j+1])/dX**2 - K * (C_temp[i-1][j]-2*C_temp[i][j]+C_temp[i+1][j])/dY**2) 
                if(C[i][j]<0):
                    C = 0


        for j in range(len(C[0])): #borda superior/inferior
            C[0][j] = C[1][j]
            C[m-1][j] = C[m-2][j]
        print(len(C))
        for i in range(len(C)): #borda esquerda/direita
            C[i][0] = C[i][1]
            C[i][n-1] =C[i][n-2]
        count+=1
        C_temp = np.copy(C)
        print("Retornou depois de {0} segundos.".format(n*dT))
        return C
K = 1       #m²/s
alpha = 1   #m/s
T = 3       #s
Q = 100     #kd/ms
Lx = 30     #m
Ly = 20     #m
a = 1/1.4
b = 60/6
dX = 0.5  #NÃO SEI PQ É 1
dY = 0.5  #^^^^^^^^^^^^


pontos_x = int((Lx / dX)) + 1
pontos_y = int((Ly / dY)) + 1

dT = ((1/(4*K)) * (dX * dY)) 
#dT = 0.2
print(dT)

results = burger(pontos_y,pontos_x,T,10*T,dT,dX,dY,alpha,Q,K)

plt.imshow(results, cmap='Reds', interpolation='nearest')
plt.colorbar()
plt.show()
