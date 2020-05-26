# -*- Coding: UTF-8 -*-
#coding: utf-8

import math
import numpy as np
import matplotlib.pyplot as plt 


def getTemp(T_real,m,alpha,dT,dX,tol,t,borda):
    beta = alpha * dT
    f_zero = alpha*dT/(dX**2)
    print("F ZEROOOOOOOOOOOOO", f_zero)
    n = 0
    T = np.copy(T_real)
    T_f = np.copy(T)

    if borda==1: #esquerda isolada
        while(n<(t/dT)):
            lista_erros = []        
            for i in range(1,m-1):
                for j in range(m-1):
                    
                    if j == 0:
                        #print(150*f_zero)
                        T[i][j] = (f_zero) * ( 2*T_f[i][1] + T_f[i+1][0] + T_f[i-1][0]) + (1 - 4 * f_zero)* T_f[i][0]
                    
                    else:
                        partX = (T_f[i][j+1] - 2*T_f[i][j] + T_f[i][j-1])/(dX**2)

                        partY = (T_f[i+1][j] - 2*T_f[i][j] + T_f[i-1][j])/(dX**2)

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
    
    if borda==2: #cima isolado
        while(n<(t/dT)):
            lista_erros = []        
            for i in range(m-1):
                for j in range(1,m-1):
                    
                    if i == 0:
                        #T[i][j] = (f_zero) * ( 2*T_f[i][1] + T_f[i+1][0] + T_f[i-1][0]) + (1 - 4 * f_zero)* T_f[i][0]
                        
                        #print((T_f[i][j+1]+T_f[i][j-1]+2*T_f[i+1][j]))
                        #print(T_f[i][j+1])
                        #print(T_f[i][j-1])
                        #print(T_f[i+1][j])
                        print( (1 - 4 * f_zero)* T_f[i][j])
                        print((f_zero) * ( 2*T_f[i][1] + T_f[i+1][0] + T_f[i-1][0]))
                        T[i][j] = (f_zero) * (T_f[i][j+1]+T_f[i][j-1]+2*T_f[i+1][j]) + (1 - 4 * f_zero)* T_f[i][j]
                        print("OLA", T[i][j])
                        
                    else:
                        partX = (T_f[i][j+1] - 2*T_f[i][j] + T_f[i][j-1])/(dX**2)

                        partY = (T_f[i+1][j] - 2*T_f[i][j] + T_f[i-1][j])/(dX**2)

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

    if borda==3: #direito isolado
        while(n<(t/dT)):
            lista_erros = []        
            for i in range(1,m-1):
                for j in range(1,m):
                    
                    if j == m-1:
                        #T[i][j] = (f_zero) * ( 2*T_f[i][1] + T_f[i+1][0] + T_f[i-1][0]) + (1 - 4 * f_zero)* T_f[i][0]
                        T[i][j] = (f_zero) *   (2*T_f[i][j-1]+T_f[i+1][j]+T_f[i-1][j]) + (1 - 4 * f_zero)* T_f[i][0]
                    else:
                        partX = (T_f[i][j+1] - 2*T_f[i][j] + T_f[i][j-1])/(dX**2)

                        partY = (T_f[i+1][j] - 2*T_f[i][j] + T_f[i-1][j])/(dX**2)

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

    if borda==4: #inferior isolado
        while(n<(t/dT)):
            lista_erros = []        
            for i in range(1,m-1):
                for j in range(1,m-2):
                    
                    if i == m:
                        T[i][j] = (f_zero) *   (T_f[i][j+1] + T_f[i][j-1] + 2* T_f[i-1][j]) + (1 - 4 * f_zero)* T_f[i][0]
                    else:
                        partX = (T_f[i][j+1] - 2*T_f[i][j] + T_f[i][j-1])/(dX**2)

                        partY = (T_f[i+1][j] - 2*T_f[i][j] + T_f[i-1][j])/(dX**2)

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

 

    else:
        while(n<(t/dT)):
            lista_erros = []        
            for i in range(1,m-1):
                for j in range(1,m-1):
                    partX = (T_f[i][j+1] - 2*T_f[i][j] + T_f[i][j-1])/(dX**2)
                    partY = (T_f[i+1][j] - 2*T_f[i][j] + T_f[i-1][j])/(dX**2)
                    T[i][j] =  T_f[i][j] + beta * (partX + partY)
                    if (T[i][j]!= 0):
                        erro = np.abs((T[i][j]-T_f[i][j])/T[i][j])
                        lista_erros.append(erro)
            
            if(np.max(lista_erros)<tol):
                print("Convergiu após {0} segundos".format(n*dT) )
                return T
            T_f = np.copy(T)
            n+=1    
        print("Retornou depois de: ",n*dT," segundos")
        print("Erro relativo máximo: ", np.max(lista_erros))
        return T_f




pontos = int(input ("Digite a quantidade de pontos: "))
t = float(input ("Digite o tempo: "))
dT = float(input ("Digite a variação do tempo: "))
tol = float(input ("Digite a tolerância: "))
q =int(input("Você tem o alpha? (s-->1/n-->0)")) 
if(q==1):
   alpha = float(input("Digite o valor do alpha:"))
elif (q==0): 
   k = float(input("Digite o K (W/m.℃): "))
   cp = float(input("Digite o Cp (J/kg.℃): "))
   ro = float(input("Digite o ro (kg/m³): "))
   alpha = k/(ro*cp)
    
tamanho = float(input("Digite o tamanho total em metros: "))
dXY = tamanho/(pontos - 1)

temperatura = float(input("Digite a temperatura dos pontos internos: "))


borda = int(input("Qual borda está isolada? (NENHUMA->0/Esquerda-->1/Cima-->2/Direita-->3/Baixo-->4) "))
left = float(input("Temperatura da borda da esquerda: "))
up = float(input("Temperatura da borda da cima: "))
right = float(input("Temperatura da borda da direita: "))
down = float(input("Temperatura da borda da baixo: "))

print("=====================")
print(alpha)
print((1/8)*(dXY**2+dXY**2)/alpha)
print("=====================")
# pontos = 10
# t = 10
# dT = 0.001 
# tol = 0.0001
# k = 0.00023      # W/m.℃ Condutividade térmica:
# cp = 897         # J/kg.℃ Calor específico:  
# ro = 0.0027   # kg/m³Densidade:
# alpha = k/(ro*cp) #difusividade (depende da condutividade, ro e calor especifico)
# tamanho = 0.4
# dXY = tamanho/(pontos - 1)
# temperatura = 0
# left = 0
# up = 150
# right = 50
# down = 0
# borda = 1

#alpha = 9.49667 * 10 e-5


T = np.full( (pontos, pontos), temperatura)

########LEONARDO BABACA NAO ESQUECA #####################################
#MACHI
# for j in range(pontos):
#     T[j][0] = left
#     T[j][-1] = right
#     T[0][j] = up
#     T[-1][j] = down

if borda ==1: #esquerda
    print("BORDA 1")
    for j in range(pontos):
        T[j][0] = left
        T[j][-1] = right
        T[0][j] = up
        T[-1][j] = down

elif borda ==2: #up
    print("BORDA 2")
    for j in range(pontos):
        T[0][j] = up
        T[j][0] = left
        T[j][-1] = right
        T[-1][j] = down
    
print(T)
results = getTemp(T,pontos,alpha,dT,dXY,tol,t,borda)


#for i in range(len(results)):
 #   print(results[i][0])


print(results.round(3))

plt.imshow(results, cmap='Reds', interpolation='nearest')
plt.colorbar()
plt.show()