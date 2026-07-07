# Program - Accept N numbers from user and store it into List
# Accept 1 another element from user and
# return frequency of that number from list

def NumFrequency(Data,No):
   Count = 0

   for i in range(len(Data)):
      
      if Data[i] == No:
          
          Count = Count +1

   return Count

def main():
    eleList = list()

    eleCount = int(input("How many number of elements you want to enter into list : "))
    
    print("Enter Elements : ",end="")

    for i in range(eleCount):

        ele = int(input())

        eleList.append(ele)

    print(f"Elements List : {eleList}")

    No = int(input("Element to Search : "))

    Ret = NumFrequency(eleList,No)

    print(f"Frequency of {No} in List is : {Ret}")

if __name__ == "__main__":
    main()