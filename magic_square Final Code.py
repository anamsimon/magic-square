from random import randrange



def MagicSquareFunction(n, missing_numbers):
    
    
    magicSquare = [[0 for x in range(n)]for y in range(n)]
    magicSquare1 = [[str(0) for x in range(n)]for y in range(n)]
    
    i = n // 2
    j = n - 1
    
    
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:

            if j == n:
                j = 0

            if i < 0:
                i = n - 1

        if magicSquare[int(i)][int(j)]:
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            magicSquare1[i][j] = num
            num = num + 1

        j = j + 1
        i = i - 1
        
    
        
    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (magicSquare[i][j]),
                end='')#

            if j == n - 1:
                print()

    a = randrange(len(magicSquare) - 1)
    b = randrange(len(magicSquare) - 1)
    ii = 0
    print("Enter ", missing_numbers , " missing numbers.")
        
    while(ii < missing_numbers):        
        magicSquare[a][b] = int(input("Enter number: "))
        magicSquare1[a][b] = "X"
        
        a = a + 1
        b = b + 1
        ii = ii + 1
    
        
    for i in range(0, n):
        for j in range(0, n):
            print(' ', (magicSquare1[i][j]),
                end='')#

            if j == n - 1:
                print()
    print()    

    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (magicSquare[i][j]),
                end='')#

            if j == n - 1:
                print()
    
    
    iSize = len(magicSquare[0])
    sum_list = []
    
    sum_list.extend([sum (lines) for lines in magicSquare])   

    for col in range(iSize):
        sum_list.append(sum(row[col] for row in magicSquare))
    
    result1 = 0
    for i in range(0,iSize):
        result1 +=magicSquare[i][i]
    sum_list.append(result1)  
    
    result2 = 0
    for i in range(iSize-1,-1,-1):
        result2 +=magicSquare[i][i]
    sum_list.append(result2)

    if len(set(sum_list))>1:
        return "Not a Magic Square"
    return "Magic Square"
          

    
    
while(True):
    num = int(input("Enter a number: "))
    if(num % 2 == 0):
        print("Invalid input")
        continue
    else:
        break

missing_numbers = randrange(4)
print()
print("missed value are : " , missing_numbers)

print()
count = 0
while(count < 3):
    result = MagicSquareFunction(num, missing_numbers)
    print(result)
    if(result == "Not a Magic Square"):
        count = count + 1
        continue
    else:
        break
