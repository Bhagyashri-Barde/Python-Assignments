# Program - Accept 1 Number and prints that
# many numbers in reverse order

def ReverseSeries(No):
    revList = []
    
    for i in range(No,0,-1):
        revList.append(i)
    
    return revList


def main():
    Value =  int(input("Enter your Number :"))

    Ret = ReverseSeries(Value)

    print("Numbers in reverse order :")
    for i in Ret:
        print(i)

if __name__ == "__main__":
    main()