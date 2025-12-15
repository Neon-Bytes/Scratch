import numpy as np

#slicing syntax -----> array[ start:stop:step ]

array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
print(array[0,3])
print(array[:,0:2])
print("this is the middle quadrant")
print(array[1:3,1:3])
print("this is the top right quadrant")
print(array[0:2,2:4])