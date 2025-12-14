import numpy as np

ages=np.array([[21,17,19,20,16,30,18,65],[39,22,15,99,18,19,20,21]])
print(ages,"\nshape of the array ages: ",ages.shape)

teenagers=ages[ages<18]
adults=ages[(ages>=18) & ((ages<65))]
seniors=ages[ages>=65]
evens=ages[ages%2==0]
odds=ages[ages%2!=0]

print(teenagers,"\nshape of the array who are less than 18:",teenagers.shape)
print(adults,"\nshape of the array who are greater than 18 and less than 65 :",adults.shape)
print(seniors,"\nshape of the array seniors: ",seniors.shape)
print(evens,odds)

#the below is slower than boolean indexing
#when filtering and creating a new array if we need to preserve the shape we use 
#Where function

adults=np.where(ages>=18,ages,-1)
print(adults)