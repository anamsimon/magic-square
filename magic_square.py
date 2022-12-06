import numpy as np
import random

#returns magic square N x N
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

#randomly generate missing numbers in the magix square
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
    
#print magic square
def print_matrix(square):
    for i in square:
        print('\t'.join(map(str, i)))
    print('------------')
    
#calculate magix sum
def MagicSquareSum(array) :
    n = len(array)
    sum1=0
    for i in range(n):
        sum1+=array[i][i]
    return sum1  

#main program flow
def main():
    cont = "y"
    while(cont=='y'):
        try:
            N = int(input("Magic Number N X N ? "))
            
            missing_numbers = int(input("Missing Numbers ? "))
            
            magic_square = generate_magic_square(N)
            missing_square = generate_missing_number(magic_square,N,missing_numbers)
            
            count = 0
            limit = missing_numbers + 2
            while(count < limit and missing_numbers > 0):
                    count=count + 1
                    print_matrix(missing_square)
                    print("Guess missing number X")
                    row = int(input("Row (1...N): "))
                    col = int(input("Column (1...N): "))
                    guess = int(input("Missing number: "))
                    
                    if(magic_square[row-1][col-1]==guess):
                        print("Correct")
                        missing_square[row-1][col-1]=guess
                        missing_numbers=missing_numbers - 1
                    else:
                        print("Wrong guess")
                    print("Attempt remaining ", limit - count)
                    print('------------')
                        
            if(missing_numbers==0):
                print("You have won!")
            else:
                print("Game Over! Sorry you lost.")
            print("The Magic sum is ", MagicSquareSum(magic_square))
            
            cont = input("Play again? [y/n] ")
        
        except:
            print("Something went wrong. Play again.")
main()
print("Thank you for playing the game. Bye")
