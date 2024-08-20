import numpy as np
arr=np.arange(0,11)
print(arr)

trozoArr= arr[0:6]
print(trozoArr) #Pedimos que nos traiga los número desde 0 a 6. Pero etner en cuenta que el 6 no esta incluido
trozoArr[:]=0
print(trozoArr) # Todos los número fueron cambiados por cero 
print(arr) # arr era el arreglo original  y ahora vemos que los 6 primeros numeros de 6 seis primera posiciones estan en cero porque son parte de trozoArr que fue la variable donde indicamos que los seis primeros numeros sean cambiados por cero
arr_copy=arr.copy()
arr_copy[:]=100
print (arr_copy) #Ahora todos los números se conviertiron en 100 pero dentro de la copia que se creo, si usamos el arreglo original, osea arr, los números no estarán cambiados
print (arr)