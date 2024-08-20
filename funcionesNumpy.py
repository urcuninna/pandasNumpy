import numpy as np

arr=np.random.randint(1,20,10)
print (arr)# Pedimos que nos de 10 números al azar de 1 a 20

matriz= arr.reshape(2,5)
print(matriz) #Ahora pedimos que el array lo acomode en un estructura de matriz  de 5 columnas y 2 filas

maximo=arr.max()
print(maximo)# Con max hacemos que del array nos traiga el número mayor

maximo=matriz.max()
print(maximo)# Con max hacemos que de la matriz nos traiga el número mayor

a=np.array([[1,2],[3,4]])
print(a)#Creamos un array de dos dimensiones
b=np.array([[5,6]])
print (b)#Creamos un array de una dimensión

c=np.concatenate((a,b), axis=0) 
#axis=0: Concatenación a lo largo del primer eje (filas). Esto significa que los arrays se apilan uno debajo del otro, creando un array más grande en términos de filas.
#axis=1: Concatenación a lo largo del segundo eje (columnas). En este caso, los arrays se colocan uno al lado del otro, creando un array más grande en términos de columnas.
print(c)# Concatemos el array a con el array b y ahora son un solo array

