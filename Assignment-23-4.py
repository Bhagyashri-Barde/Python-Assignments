# Program - Count how many Odd number exist  
# Between from 1 To N using Pool.map()

import multiprocessing
import os

def CountOdd(Data):
    Count = 0

    for no in range(1,Data + 1):

        if no % 2 != 0:

            Count = Count + 1
    
    print("Process ID : ",os.getpid())        
    print(f"Input Number : {Data}")
    print(f"Odd Numbers Count : {Count} \n")

def main():
    numList = [1000000,2000000,3000000,4000000]

    eObj = multiprocessing.Pool()

    eObj.map(CountOdd,numList)

    eObj.close()
    eObj.join()

    pass
if __name__ == "__main__":
    main()
