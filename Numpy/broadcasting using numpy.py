import numpy as np

#broadcasting

array1=np.array([[1,2,3,4]])
array2=np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

broadcast=array1*array2

print(broadcast)


array3=np.array([[1,2,3,4,5,6,7,8,9,10]])
print(array3.shape)
array4=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(array4.shape)
broadcast1=array3+array4
print(broadcast1)