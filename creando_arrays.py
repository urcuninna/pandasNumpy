import numpy as np

#lista=list(range(0-10)) empieza en 0 y en 10 para y no se incluye
lista= np.arange(0,10)
lista = np.arange(0,20)
lista= np.arange (0,20,2) #va de 0 a 20 de dos en dos
lista=np.zeros(3) #array de tres ceros
lista=np.zeros((10,10)) #crea un array de 10 x 10 de ceros
lista=np.ones((10,5)) #Crea un array de 10x5 de ceros
lista=np.linspace(0,10,10)
lista=np.linspace(0,10,100)
lista=np.eye(4)
lista= np.random.rand()#Nos da un un valor aleatorio
lista=np.random.rand(4) #Nos da 4 valores aleatorios
lista= np.random.rand(4,5) #Nos da una matriz de 4x5 con un total de 20 números
lista=np.random.randint(1,15) #Nos da un numero aleatorio entre el rango que esta en los parentesis, en este caso de 1 a 15
lista= np.random.randint(1,100,(10,10))
print(lista)