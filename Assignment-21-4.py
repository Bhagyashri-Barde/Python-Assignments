'''
Program - Design Python Application 
Create 2 Threads
1) Thread1 - Should Compute Sum of elements from a list

2) thread - Should Compute Product of elements from the same list

Return the result to the main thread and display them

'''
import threading 

def Sum(Data,Ret):

    total = 0

    for i in Data:

        total = total + i

    Ret["Sum"]  = total

def Product(Data,Ret):
    prod = 1

    for i in Data:

        prod = prod * i

    Ret["Product"]  = prod

def main():
    numList = [1,2,3,4,5]

    Ret = {}

    print("List of Numbers : ",numList)

    t1 = threading.Thread(target=Sum,args=(numList,Ret,))

    t2 = threading.Thread(target=Product,args=(numList,Ret,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum is :",Ret["Sum"])

    print("Product is :",Ret["Product"])

if __name__ == "__main__":
    main()