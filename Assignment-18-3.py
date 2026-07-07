# Program - Accept N numbers from user and store it into List
# Return Minimum number from that List

def DisplayMin(Data):
    MinElement = Data[0]
    # for i in range(len(Data)):                    
    #     for j in range((i+1),len(Data)):
    #         if Data[i] > Data[j]:            
    #             Data[i],Data[j] = Data[j],Data[i]        # Sorting
    
    # return Data[0]

    for i in range(1,len(Data)):

        if MinElement > Data[i]:

            MinElement = Data[i]
            
    return MinElement
    
def main():
    eleList = list()

    eleCount = int(input("How many number of elements you want to enter into list : "))
    
    print("Enter Elements : ",end="")

    for i in range(eleCount):

        ele = int(input())

        eleList.append(ele)

    print(f"Elements List : {eleList}")
    
    Ret = DisplayMin(eleList)

    print(f"Minimum Number From List is : {Ret}")

if __name__ == "__main__":
    main()