# Program - Calculates Factorial of multiple numbers
# Simulteniously using Pool.map()
# Display - 1) Process ID     2) Input Number     3) Factorial

import multiprocessing
import os

def Factorial(No):

    result = 1

    for i in range(1,No+1):

        result = result * i

    print("Process ID : ",os.getpid())
    
    print(f"Factorial of {No} is : {result}\n")

    return result

def main():
    NumList = list()
    Ret = []

    elecount = int(input("Enter Number of Elements in List : "))

    print("Enter Elements : ",end="")

    for i in range(elecount):
        
        NumList.append(int(input()))

    
    
    fObj = multiprocessing.Pool()

    Ret =  fObj.map(Factorial,NumList)

    fObj.close()
    fObj.join()

    print("List is : ",NumList)
    print("Factorial is : ",Ret)
    
if __name__ == "__main__":
    main()
