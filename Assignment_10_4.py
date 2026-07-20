# Program - Accept 1 number and
# Prints All Even Numbers till that Number

print("-------------------------------------")
print("------------ Even Numbers -----------")
print("-------------------------------------")

def ChkEven(No):
    evenList = []
    
    for i in range(1,No+1):

        if( i % 2 == 0 ):
             evenList.append(i)

    return evenList
            

def main():

    Value = int(input("Enter Your Number : "))

    print("Even Numbers From 1 To",Value)

    Ret = ChkEven(Value)

    for i in Ret:
        print(i)

if __name__ == "__main__":
    main()