import numpy as np
import random

def generate_magic_square(N):

    magic_square = np.zeros((N,N), dtype=int)
    n = 1
    i, j = 0, N//2

    while n <= N**2:
        magic_square[i, j] = n
        n += 1
        newi, newj = (i-1) % N, (j+1)% N
        if magic_square[newi, newj]:
            i += 1
        else:
            i, j = newi, newj

    return magic_square

def generate_missing_number(magic_square, N, missing_number):

    missing_square = [[''] * N for i in range(N)]

    for i in range (N):
         for j in range (N):
            missing_square[i][j] = str(magic_square[i,j])
    n = 1
    while n <= missing_number:
        i,j = random.randint(0,N-1), random.randint(0,N-1)
        if missing_square[i][j] != "X":
            missing_square[i][j] = "X"
            n += 1
    return missing_square

def print_matrix(square):
    for i in square:
        print('\t'.join(map(str, i)))

N = int(input("Magic Number N X N ? "))

missing_numbers = int(input("Missing Numbers ? "))

magic_square = generate_magic_square(N)
missing_square = generate_missing_number(magic_square,N,missing_numbers)

print_matrix(magic_square)
print_matrix(missing_square)