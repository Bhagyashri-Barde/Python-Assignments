'''
 Program - Accept N numbers from user and store it into List
 Return Addition of all prime numbers from that list 
 Main Python file Accepts N number from user and apass each number to
 ChkPrime() Function which is Part of user defiend Module 
 Named as MarvellousNum 
 Name of the function from main python file should Be ListPrime

 '''

from MarvellousNum import *

def ListPrime(Data):
   primeList = list()
   Sum = 0
 
   for i in range(len(Data)):
       
       if (ChkPrime(Data[i])):
           primeList.append(Data[i])

   print("Prime List :",primeList)

   for i in primeList:
       Sum = Sum + i

   return Sum       
    
       

def main():
    eleList = list()

    eleCount = int(input("How many number of elements you want to enter into list : "))
    
    print("Enter Elements : ",end="")

    for i in range(eleCount):

        ele = int(input())

        eleList.append(ele)

    print(f"Elements List : {eleList}")

    Ret = ListPrime(eleList)

    print("Adition of Prime Numbers from List : ",Ret)


if __name__ == "__main__":
    main()