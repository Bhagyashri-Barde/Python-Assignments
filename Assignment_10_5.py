# Program - Accept 1 number and
# Prints All Odd Numbers till that Number

print("-------------------------------------")
print("------------- Odd Numbers -----------")
print("-------------------------------------")

def ChkOdd(No):
    oddList = []

    for i in range(1,No+1):

        if( i % 2 != 0 ):
            oddList.append(i)
            
    return oddList

def main():

    Value = int(input("Enter Your Number : "))
    
    print("Odd Numbers From 1 To",Value)

    Ret = ChkOdd(Value)

    for i in Ret:
        print(i)

if __name__ == "__main__":
    main()