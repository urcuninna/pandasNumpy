import numpy as np
arr= np.linspace(1,10,10, dtype='int8')
print(arr)
indices_con=arr>5
print(indices_con)
print(arr[indices_con])
print(arr[(arr>5)&(arr<9)])
arr[arr>5]=99
print(arr)
