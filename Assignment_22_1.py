# Program - Accepts list of integers and use
# Pool.map() to calculate the sum of Square 
# from 1 To N for every element in the list
import multiprocessing

def SquareSum(No):
    Sum = 0

    for i in range(1,No+1):

        Sum = Sum + (i ** 2)

    return Sum

def main():
   # NumList = [1000000,2000000,3000000,4000000]
    NumList = list()
    Ret = []

    elecount = int(input("Enter Number of Elements in List : "))

    print("Enter Elements : ",end="")

    for i in range(elecount):
        
        NumList.append(int(input()))

    print("List is : ",NumList)

    sObj = multiprocessing.Pool()

    Ret =  sObj.map(SquareSum,NumList)

    sObj.close()
    sObj.join()

    print("Result : ",Ret)
    
if __name__ == "__main__":
    main()