import numpy as np

array=np.array('A')
print(array.ndim)

array_1d=np.array([1,2,3,4,5])
print("dim=",array_1d.ndim,"   shape=",array_1d.shape)

array_2d=np.array([[2,3,5],
                    [7,11,13]])
print("dim=",array_2d.ndim,"   shape=",array_2d.shape)

array_3d=np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                   [['J','K','L'],['M','N','O'],['P','Q','R']],
                   [['S','T','U'],['V','W','X'],['Y','Z','_']]])
print("dim=",array_3d.ndim,"   shape=",array_3d.shape)

#now we jump to multidimensional indexing
#syntax----> array[row,col,index]

print(array_3d[1,0,2])
word=array_3d[0,1,2]+array_3d[0,0,0]+array_3d[0,2,2]+array_3d[2,0,1]+array_3d[0,2,1]
print(word)