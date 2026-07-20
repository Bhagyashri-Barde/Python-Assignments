# Program - Calculates Factorial of multiple numbers  
# Simulteniously using multiprocessing.Pool

import multiprocessing
import os

def Factorial(Data):
    print("Process ID : ",os.getpid())

    
    factorial = 1

    for no in range(1,Data + 1):

        factorial = factorial * no
            
    print(f"Input Number : {Data}")
    print(f"Factorial of {no} is : {factorial} \n")

def main():
    numList = [10,15,20,25]

    eObj = multiprocessing.Pool()

    eObj.map(Factorial,numList)

    eObj.close()
    eObj.join()

    pass
if __name__ == "__main__":
    main()
