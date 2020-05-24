# -*- Coding: UTF-8 -*-
#coding: utf-8

import math
import numpy as np
import matplotlib.pyplot as plt 


# t_list = [0,20,20,20,20,20,20,20,20,20,0]
# x = [0,0.1,0.2,0.3,0.4,0.5]

tol = 1e-4

########
def getTemp(m,alpha,dT,dXY,tol,t,receive):
    beta = alpha * dT
    f_zero = alpha*dT/(dXY**2)
    n = 0
    T = np.copy(receive)
    print(T)
    T_f = np.copy(T)
    print(T_f)
    while(n<(t/dT)):
        lista_erros = []        
        for i in range(1,m-1):
            for j in range(m-1):
                
                if j == 0:
                    
                    #print(150*f_zero)
                    T[i][j] = (f_zero) * ( 2*T_f[i][1] + T_f[i+1][0] + T_f[i-1][0]) + (1 - 4 * f_zero)* T_f[i][0]
                
                else:   
                    partX = (T_f[i][j+1] - 2*T_f[i][j] + T_f[i][j-1])/(dXY**2)
                    print(partX)
                    partY = (T_f[i+1][j] - 2*T_f[i][j] + T_f[i-1][j])/(dXY**2)
                    print(partY)
                    T[i][j] =  T_f[i][j] + beta * (partX + partY)
                
                print(T[i][j])
                if (T[i][j]!= 0):
                    erro = np.abs((T[i][j]-T_f[i][j])/T[i][j])
                    lista_erros.append(erro)
        print(lista_erros)
        if(np.max(lista_erros)<1e-8):
            print("Convergiu após {0} segundos".format(n*dT) )
            return T
        
            
        
        
        T_f = np.copy(T)
        n+=1    
    print("Retornou depois de: ",n*dT," segundos")
    print("Erro relativo máximo: ", np.max(lista_erros))
    return T_f


#########


dT = 0.001    #s

k = 0.23e3      # W/m.℃ Condutividade térmica:
cp = 897         # J/kg.℃ Calor específico:  
ro = 2.7e3   # kg/m³Densidade:
alpha = k/(ro*cp) #difusividade (depende da condutividade, ro e calor especifico)
pontos = 10
tamanho = 0.4
dXY = tamanho/(pontos - 1)
print("DYGUBFJVGYBF : ", dXY)

#pontos = int(input ("Digite a quantidade de pontos: "))
#q =int(input("Você tem o alpha? (s-->1/n-->0)")) 
#if(q==1):
#    alpha = input("Digite o valor do alpha:")
#elif (q==0): 
#    k = float(input("Digite o K (W/m.℃): "))
#    cp = float(input("Digite o Cp (J/kg.℃): "))
#    ro = float(input("Digite o ro (kg/m³): "))
#    alpha = k/(ro*cp)
    
#tamanho = int(input("Digite o tamanho total em metros: "))
#dXY = tamanho/(pontos - 1)

#temperatura = float(input("Digite a temperatura dos pontos internos: "))
temperatura = 0
T = np.full( (pontos, pontos),temperatura )


#borda = int(input("Qual borda está isolada? (NENHUMA->0/Esquerda-->1/Cima-->2/Direita-->3/Baixo-->4) "))
#left = float(input("Temperatura da borda da esquerda: "))
#up = float(input("Temperatura da borda da cima: "))
#right = float(input("Temperatura da borda da direita: "))
#down = float(input("Temperatura da borda da baixo: "))
borda = 1
left = 43949
up =150
right = 50
down = 0

for j in range(pontos):
    T[0][j] = up
    T[j][0] = left
    T[j][-1] = right
    T[-1][j] = down
    
if borda == 1:
    for j in range(pontos):
        T[j][0] = temperatura
if borda == 2:
    for j in range(pontos):
        T[0][j] = temperatura
if borda == 3:
    for j in range(pontos):
        T[j][-1] = temperatura
if borda == 4:
    for j in range(pontos):
        T[-1][j] = temperatura

print(T)
results = getTemp(pontos,alpha,dT,dXY,tol,10, T)

# getTemp(T_a,m,alpha,dT,dXY,tol,t):

#for i in range(len(results)):
 #   print(results[i][0])


print(results.round(2))

plt.imshow(results, cmap='Reds', interpolation='nearest')
plt.colorbar()
plt.show()

