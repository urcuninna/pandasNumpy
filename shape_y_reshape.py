import numpy as np
#Generamos números aleatorios entre 1 y 10 con una estructura de 3x2
arr=np.random.randint(1,10,(3,2))
#imprimir la forma del arreglo
print("forma original: ", arr.shape)
print(arr) #tres filas y dos columnas
#cambiamos la forma del arreglo con una forma de (1,6)
arr_reshaped=arr.reshape(1,6)
#Imprimimos el arreglao después del cambio de la forma
print("Arreglo después del reshape: ", arr_reshaped)#El mismo arr pero ahora 1 fila y 6 columnas