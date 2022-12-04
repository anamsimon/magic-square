#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import random

def generate_magic_square(N):

    magic_square = np.zeros((N,N), dtype=int)
    n = 1
    i, j = 0, N//2

    while n <= N**2:
        magic_square[i][j] = n
        n += 1
        newi, newj = (i-1) % N, (j+1)% N
        if magic_square[newi][newj]:
             i = i+ 1
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
    print('---')

N = int(input("Magic Number N X N ? "))

missing_numbers = int(input("Missing Numbers ? "))

magic_square = generate_magic_square(N)
missing_square = generate_missing_number(magic_square,N,missing_numbers)

print_matrix(magic_square)
print_matrix(missing_square)



"""
Code Wroten by MD ABDUR RAFIQ ----152028
"""

from array import *

arr = missing_square

count = 0
while(count < 3):
    
        n = int(input("Enter the number of the row: "))
        m = int(input("Enter the number of the Col: "))
        p = int(input("Enter the number of the Value: "))
        
        print(" Array")
        for _ in arr:
            for i in _:
                print(i,end=" ")
            print()
        arr[n][m]=p 
        print("New Array")
        for _ in arr:
            for i in _:
                print(i,end=" ")
            print()
        count = count + 1
        if count == missing_numbers:
            break
        else:
            print("Hiii")
        
            
    
def MagicSquareCheck( array) :
  n = len(array)
  sum1=0
  sum2=0
  for i in range(n):
    sum1+=array[i][i]
    sum2+=array[i][n-i-1]
  if not(sum1==sum2):
    return False
  for i in range(n):
    sum_r=0
    sum_c=0
    for j in range(n):
      sum_r+=array[i][j]
      sum_c+=array[j][i]
    if not(sum_r==sum_c==sum1):
      return False
    
  return True
         
     

array = [list( map(int,i) ) for i in arr]

if (MagicSquareCheck(array)) :
    print( "Thanks Right Choice Its a Magic Square")
else :
    print( "Not a magic Square please try again")
    
    
"""End Code Develope by Rafiq"""

