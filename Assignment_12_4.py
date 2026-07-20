# Program - Accept 1 Number and prints that
# many numbers starting from 1

def numSeries(No):

    return range(1,No+1)

def main():
    Value =  int(input("Enter your Number :"))

    Ret = numSeries(Value)

    print("Numbers From 1 To",Value,"are : ")
    for i in Ret:
        print(i)

if __name__ == "__main__":
    main()