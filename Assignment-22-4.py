'''
Program - Calculates

1^5 + 2^5 + 3^5 + ..... + N^5

For multiple values of N simulteniously using Pool
Measure total execution time

'''
import multiprocessing
import time

def Power5(No):
     Sum  = 0

     for i in range(1,No+1):
         
         Sum = Sum + (i ** 5) 

     return Sum

def main():
    NumList = list()
    Ret = []

    elecount = int(input("Enter Number of Elements in List : "))

    print("Enter Elements : ",end="")

    for i in range(elecount):
        
        NumList.append(int(input()))

    print("List is : ",NumList)
    
    Start_time = time.perf_counter()

    fObj = multiprocessing.Pool()

    Ret =  fObj.map(Power5,NumList)

    fObj.close()
    fObj.join()

    End_time = time.perf_counter()

    print("Result : ",Ret)

    print(f"Total Execution Time is : {End_time - Start_time}")
    
if __name__ == "__main__":
    main()