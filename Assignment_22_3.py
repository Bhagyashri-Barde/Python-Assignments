# Program - For every number in the list 
# Count how many prime numbers exists between
# 1 and N using multiprocessing Pool
# Display total Prime count for each number

import multiprocessing

def ChkPrime(No):
    pCount = 0

    for ele in range(2,No+1):

        Count = 0

        for i in range(1,ele+1):
            
            if(ele % i == 0):

                Count = Count + 1
    
        if Count == 2:
            
            pCount = pCount + 1

    return pCount

def main():
    NumList = list()
    Ret = []

    elecount = int(input("Enter Number of Elements in List : "))

    print("Enter Elements : ",end="")

    for i in range(elecount):
        
        NumList.append(int(input()))

    
    
    fObj = multiprocessing.Pool()

    Ret =  fObj.map(ChkPrime,NumList)

    fObj.close()
    fObj.join()

    print("List is : ",NumList)
    print("Prime Number count : ",Ret)
    
if __name__ == "__main__":
    main()
