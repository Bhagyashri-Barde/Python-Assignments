'''
Program - Contain filter(),map(),reduce()
Contain List of Numbers,numbers are ceepted from users
filter() - All Even Numbers
map() - Calculates its square
reduce() - return Addition of all that Numbers

'''
from functools import reduce

FilterData = lambda No : No % 2 == 0

Increase =lambda No : No * No

NumProduct = lambda No1, No2 : No1 + No2 
   
def main():
   numList = list()

   eleCount = int(input("How many numbers you want to enter in list :"))
   
   print("Enter Elements : ",end="")
   
   for i in range(eleCount):
       
       numList.append(int(input()))

   print(f"List is: {numList}")

   FData = list(filter(FilterData,numList))

   print("List After Filter (Even Numbers) :",FData)

   MData = list(map(Increase,FData))

   print("List After Map (Square of Numbers):",MData)

   RData = reduce(NumProduct,MData)

   print("Output of reduce (Addition Of Numbers):",RData)


if __name__ == "__main__":
    main()