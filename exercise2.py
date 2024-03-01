import numpy as np

# a. Create a null vector of size 10 but the fifth value which is 1
nullvector = np.zeros((10), dtype=int)
nullvector[5] = 1
#print (nullvector)

# b. Create a vector with values ranging from 10 to 49
vector = np.arange(40) + 10
#print (vector)

# c. Reverse a vector (first element becomes last)
reversedvector = vector[::-1]
#print (reversedvector)

# d. Create a 3x3 matrix with values ranging from 0 to 8
matrix = np.arange(9).reshape(3,3)
#print (matrix)

# e. Find indices of non-zero elements from [1,2,0,0,4,0]
array = np.array([1,2,0,0,4,0])
nonzero = np.nonzero(array)
#print (nonzero)

# f. Create a random vector of size 30 and find the mean value
randomvector = np.random.random(30)
#vectorlist = list (randomvector)
#print (vectorlist)
mean = np.mean(randomvector)
#print (mean)

# g. Create a 2d array with 1 on the border and 0 inside
#n = int(input("Insert the size of the first dimension: "))
#m = int(input("Insert the size of the second dimension: "))
#twoDarray = np.zeros(n * m).reshape(n,m)
#twoDarray [0] = 1
#twoDarray [n-1] = 1
#twoDarray [:,0] = 1
#twoDarray [:,m-1] = 1
#print (twoDarray)

# h. Create a 8x8 matrix and fill it with a checkerboard pattern
x = np.zeros((8, 8), dtype=int)
x[1::2, ::2] = 1
x[::2, 1::2] = 1
#print(x)

# i. Create a checkerboard 8x8 matrix using the tile function
a = np.zeros((8), dtype=int)
a [::2] = 1
b = np.zeros((8), dtype=int)
b [1::2] = 1
c = np.append(a,b)
#print (np.tile(c, 4).reshape(8,8))

# j. Given a 1D array, negate all elements which are between 3 and 8, in place
oneDarray = np.arange(11)
oneDarray[4:8] = -oneDarray[4:8]
#print(oneDarray)

# k. Create a random vector of size 10 and sort it
randomvector = np.random.random(10)
#print (np.sort(randomvector))

# l. Consider two random arrays A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A, B) 
#print (equal)

# m. How to calculate the square of every number in an array in place (without creating temporaries)?
Z = np.arange(10, dtype=np.int32)
np.square(Z, out=Z)
#print(Z)

# n. How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = diagonal = np.diagonal(C)
print(diagonal)