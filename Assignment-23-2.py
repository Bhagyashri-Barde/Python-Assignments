# Program - Using multiprocessing.Pool 
# Calculate the sum of all Odd numbers from 1 To N

import multiprocessing
import os

def OddSum(Data):
    Sum = 0

    for no in range(1,Data + 1):

        if no % 2 != 0:

            Sum = Sum + no
        
    print("Process ID : ",os.getpid())        
    print(f"Input Number : {Data}")
    print(f"Sum Of Odd Numbers : {Sum} \n")

def main():
    numList = [1000000,2000000,3000000,4000000]

    eObj = multiprocessing.Pool()

    eObj.map(OddSum,numList)

    eObj.close()
    eObj.join()

    pass
if __name__ == "__main__":
    main()
