# -*- Coding: UTF-8 -*-
#coding: utf-8
##imports
import math
import numpy as np
import matplotlib.pyplot as plt 
# 0    0    0 
# 0    0.03 0 
# 0.03 0    0
# 0.03 0.03 0

t_base = 350 #K
t_ambiente = 300 #K
h = 15 #W/m²K
k = 200 #W/mK condutividade_termica
w = 0.03
t = 0.03
l = 0.3
x = l/2
temp = 0
Ac=w*t
P=2*    w + 2*t
m = math.sqrt((h*P)/k*Ac)
#x_list = np.linspace(0,0.3,4)
x_list = [0,0.05,0.1,0.15,0.2,0.25,0.3]
t = []

for x in x_list:
    formula = (np.cosh(m*(l-x)) + (h/m*k)*np.sinh((l-x)*m)) / (np.cosh(l*m)+(h/m*k)*np.sinh(l*m))
    t.append((formula*(t_base-t_ambiente))+t_ambiente)

print(len(x_list))
print(len(t))
print(t)
print(x_list)
plt.plot(x_list,t,'ro')
plt.show()


#Tinf(-form+1)
#transferencia de calor especificada por conveccao
#condicao na extremidade
#a manu é idiota