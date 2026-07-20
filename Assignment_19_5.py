'''
Program - Contain filter(),map(),reduce()
Contain List of Numbers,numbers are ceepted from users
filter() - All Prime Numbers
map() - Multiply each Number by 2
reduce() - return Maximum Number

'''
from functools import reduce
def ChkPrime(No):
    count = 0

    for i in range(1,No+1):
        if No % i == 0:
            count = count + 1
    if count == 2:
        return True
    else:
        return False

Multiply = lambda No: No * 2

ChkMax = lambda No1, No2: No1 if No1 > No2 else No2
    
   
def main():
   numList = list()

   eleCount = int(input("How many numbers you want to enter in list :"))
   
   print("Enter Elements : ",end="")
   
   for i in range(eleCount):
       
       numList.append(int(input()))

   print(f"List is: {numList}")

   FData = list(filter(ChkPrime,numList))

   print("List After Filter (Prime Numbers) :",FData)

   MData = list(map(Multiply,FData))

   print("List After Map (Number X 2) :",MData)

   RData = reduce(ChkMax,MData)

   print("Output of reduce (Maximum Number):",RData)


if __name__ == "__main__":
    main()