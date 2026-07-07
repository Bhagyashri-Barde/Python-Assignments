# Program - Accept N numbers from user and store it into List
# Return addition of all elements from that List

from functools import reduce

Addition = lambda No1,No2 : No1 + No2
    
def main():
    eleList = list()

    eleCount = int(input("How many number of elements you want to enter into list : "))
    
    print("Enter Elements : ",end="")

    for i in range(eleCount):

        ele = int(input())

        eleList.append(ele)

    print(f"Elements List : {eleList}")
    
    Ret = reduce(Addition,eleList)

    print(f"Addition of list elemnts is : {Ret}")

if __name__ == "__main__":
    main()