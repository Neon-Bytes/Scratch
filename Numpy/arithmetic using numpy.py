import numpy as np
 
 #scalar arithmetic

array=np.array([np.pi,4.76,6.41,7.54])
print(array-1)
print(array+1)
print(array//2)
print(array*2)
print(array%2)
print(array**5)

#vectorised maths functions

print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))

#this is the pi 
print(np.pi)

radii=np.array([1,2,3])

area=np.pi*radii**2
print("areas=",area)



array1=np.array([1,2,3])
array2=np.array([2,4,6])
print(array1+array2)
print(array1*array2)
print(array1+array2)
print(array1**array2)

scores=np.array([23,78,98,100,69,56])

print(scores==100)
print(scores>=60)
print(scores<60)

scores[scores<60]=0
scores[scores>=60]=1 
print(scores)