from random import randint
from main import *
def multiplicar(matriz1,matriz2):
    matriz_m=[[0]*n for i in range(n)]
    for x in range(n):
        for y in range(n):
            for z in range(n):
                matriz_m[x][y]+=matriz1[x][z]*matriz2[z][y]
            if matriz_m[x][y]>=1:
                matriz_m[x][y]=1
    return matriz_m
def sellega(inicial,final,cont,matriz):
    si=False
    for i in range(cont):
        if i==0:
            matriz_m=multiplicar(matriz,matriz)
        else:
            matriz_m=multiplicar(matriz_m,matriz)
        if matriz_m[inicial][final]==1:
            print(i)
            return True
    return False
cont=0
for i in range(len(matriz_ciudad)):
    for j in range(len(matriz_ciudad)):
        if matriz_ciudad[i][j]==1:
            cont+=1
print(sellega(12,51,cont,matriz_ciudad))
