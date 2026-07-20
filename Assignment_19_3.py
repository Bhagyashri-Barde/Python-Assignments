'''
Program - Contain filter(),map(),reduce()
Contain List of Numbers,numbers are ceepted from users
filter() - no >= 70 and no <= 90
map() - increase each number by 10
reduce() - return product of all that numbers

'''
from functools import reduce

FilterData = lambda No : True if (No >= 70 and No <= 90) else False

Increase =lambda No : No + 10

NumProduct = lambda No1, No2 : No1 * No2 
   
def main():
   numList = list()

   eleCount = int(input("How many numbers you want to enter in list :"))
   
   print("Enter Elements : ",end="")
   
   for i in range(eleCount):
       
       numList.append(int(input()))

   print(f"List is: {numList}")

   FData = list(filter(FilterData,numList))

   print("List After Filter (No >= 70 and No <= 90):",FData)

   MData = list(map(Increase,FData))

   print("List After Map (No + 10):",MData)

   RData = reduce(NumProduct,MData)

   print("Output of reduce (Product of Numbers):",RData)


if __name__ == "__main__":
    main()