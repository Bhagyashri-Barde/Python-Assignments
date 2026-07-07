# Program - Accept N numbers from user and store it into List
# Return Maximum number from that List

def DisplayMax(Data):
    MaxElement = Data[0]
    # for i in range(len(Data)):                    
    #     for j in range((i+1),len(Data)):
    #         if Data[i] < Data[j]:            
    #             Data[i],Data[j] = Data[j],Data[i]        # Sorting
    
    # return Data[0]

    for i in range(1,len(Data)):

        if MaxElement < Data[i]:

            MaxElement = Data[i]
            
    return MaxElement
    
def main():
    eleList = list()

    eleCount = int(input("How many number of elements you want to enter into list : "))
    
    print("Enter Elements : ",end="")

    for i in range(eleCount):

        ele = int(input())

        eleList.append(ele)

    print(f"Elements List : {eleList}")
    
    Ret = DisplayMax(eleList)

    print(f"Maximum Number From List is : {Ret}")

if __name__ == "__main__":
    main()