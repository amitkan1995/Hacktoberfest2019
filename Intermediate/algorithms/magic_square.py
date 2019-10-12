#Program to print MAGIC SQUARE for n elements
#Importing numpy lib
import numpy as np

# Only work for odd numbers
N  =  # For N X N matrix
magic_square = np.zeros((N,N), dtype=int) #Initializing matrix with zero

n = 1
i, j = 0, N//2

while n <= N**2: 
    #Tells where number 1 is going to stored in matrix.. Can be many ways
    magic_square[i, j] = n
    n += 1 #Next number to be stored in matrix
    # New position of next number can be found out using it 
    newi, newj = (i-1) % N, (j+1)% N
    #print(newi," ",newj)
    print(magic_square[newi, newj])
    if magic_square[newi, newj]: #To check if place is occupied or not
        i += 1
    else:
        i, j = newi, newj

print(magic_square)