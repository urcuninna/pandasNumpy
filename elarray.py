import numpy as np

lista=[1,2,3,4,5,6,7,8,9]
#print(lista) 
np.array(lista) #Se convierte en array
arr=np.array(lista)
print(arr)
print(type(arr))#Nos muestra el tipo de dato que es arr
matriz=[[1,2,3],[4,5,6],[7,8,9]]
matriz=np.array(matriz)
print(matriz)
print(arr[1])
print(arr[0]+arr[5])
print(matriz[0]) #Nos muestra la fila 0 de la matriz
print(matriz[1])
print(matriz[2])
print(matriz[0,2]) #Son coordenadas del dato que queremos recuperar: fila 0 columna 2
print(matriz[1,1])
print(arr[:6]) #toma el primer numero hasta el limite de la posicion 6
print(arr[2:]) #toma la posición 2 hasta el final
print(arr[:]) #Toma todos los numeros
print(arr[::3]) #Desde la posicion 0 y cuenta de tres en tres
print(arr[-1]) #Imprime el último número
print(arr[-3:]) #toma los tres ultimos numeros y los imprime
print(matriz[1:]) #toma las filas desde la posicón 1 hasta el final
print(matriz[1:,0:2]) #Toma desde la fila 1 hasta el final y desde la columna 0 hasta la 2(excluyendo la columna 2)