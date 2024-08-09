import numpy as np
scalar=np.array(45)#Un scalar en solo un elemento dentro de un array. Los escalares son cantidades que solo tienen magnitud (o tamaño), mientras que los vectores tienen tanto magnitud como dirección
print(scalar) #Imprime el scalar
print(scalar.ndim) #Imprime la dimension del scalar. En este caso la dimensión es 0
vector=np.array([1,2,3,4])#Un scalar es una lista de elementos. Lo vectores se componene de 1 dimensión
print(vector) #Imprime el vector
print(vector.ndim) #Imprime la dimension del vector . Su dimension es 1
matriz=np.array([[1,2,3],[4,5,6]])#Un scalar es una tabla u hoja de calculo en un array. Lo vectores se componene de 2 dimensiones
print(matriz) #Imprime la matrix
print(matriz.ndim) #Imprime la dimension de la matriz . Su dimension es 2
tensor=np.array([[[1,2,3],[4,5,6],[7,8,9],[0,2,45]],[[1,2,3],[4,5,6],[7,8,9],[0,2,45]]])#Un tensor es una forma de organizar los datos más compleja. Los vectores se componene de mas de 2 dimensiones
print(tensor) #Imprime el tensor
print(tensor.ndim) #Imprime la dimension del tensor . Su dimension es mayor a 2

#AGREGAR O ELIMINAR DIMENSIONES
vector2=np.array([1,2,3],ndmin=10)#Agrega 10 dimensiones
print(vector2) #Imprime el vector
print(vector2.ndim)

#EXPANDIR
expand= np.expand_dims(np.array([1,2,3]), axis=0)#expande dimensiones
print(expand)
print(expand.ndim)

#ELIMINAR DIMENSIONES QUE NO SE ESTAN USANDO
print(vector2,vector2.ndim)
vector_2=np.squeeze(vector2)
print(vector_2, vector2.ndim)