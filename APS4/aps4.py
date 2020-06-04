# -*- Coding: UTF-8 -*-
#coding: utf-8
import math
import matplotlib.pyplot as plt 
import numpy as np


def burger(m,n,T,t,dT,dX,dY, alpha, Q, K,pos_x,pos_y):
    count = 0  
    C = np.zeros((m,n))   
    C_temp = np.copy(C)
    q = Q/(dX*dY)
    print(q)
    while(count-1<2):
        for i in range(1,m-1):
            for j in range(1,n-1):
                v = alpha * math.sin(math.pi*j*dX/5)
                parte2 =  alpha*(C_temp[i][j+1]-C_temp[i][j-1])/(2*dX)
                parte3 =  v*(C_temp[i-1][j]-C_temp[i+1][j])/(2*dY)
                parte4 = (C_temp[i][j+1]-2*C_temp[i][j]+C_temp[i][j-1])/(dX**2)
                parte5 = (C_temp[i-1][j]-2*C_temp[i][j]+C_temp[i+1][j])/(dY**2)
                if ((count*dT<=T) and i==pos_y and j==pos_x ):
                    C[i][j] = C_temp[i][j] - dT * ( parte2 + parte3 - K * (parte4  + parte5  )- q )
                else:
                    #v = alpha * math.sin(math.pi*j*dX/5)
                    C[i][j] = C_temp[i][j] - dT*(parte2 + parte3 - K * (parte4 + parte5))
                
                
                if(C[i][j]<0):
                    C[i][j] = 0

        for j in range(len(C[0])): #borda superior/inferior
            C[0][j] = C_temp[1][j]
            C[m-1][j] = C_temp[m-2][j]
            
        for i in range(len(C)): #borda esquerda/direita
            C[i][0] = C_temp[i][1]
            C[i][n-1] = C_temp[i][n-2]

        count+=1
        C_temp = np.copy(C)
    print("Retornou depois de {0} segundos.".format(count*dT))
    return C
K = 1      #m²/s
alpha = 1   #m/s
T = 3       #s tempo despejo
Q = 100     #kg/ms
Lx = 30     #m
Ly = 20     #m
a =  0.5    #round(1/1.4)   #round(1/1.4,2)
b = 60/6
dX = 0.5  #
dY = 0.5  #

index_a = int(a/dX)
index_b = int(b/dY)


print(index_a,index_b)
pontos_x = int((Lx / dX)) + 1
pontos_y = int((Ly / dY)) + 1
dT = ((1/(4*K)) * (dX * dY)) 
T_total = 10 * T  #tempo total

results = burger(pontos_y,pontos_x,T,T_total,dT,dX,dY,alpha,Q,K,index_a, index_b)
#print(results[40][40])

plt.imshow(results, cmap='jet', interpolation='nearest')
plt.title("Resultado após duas iterações")
plt.gca().invert_yaxis()
plt.colorbar()
plt.show()
