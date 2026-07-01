# Program - Accept 1 number and
# Prints its factors

def Factor(No):
    factorsList = []

    for i in range(1,No+1):

        if No % i == 0:
            factorsList.append(i)
            
    return factorsList
            
def main():
    Value = int(input("Enter your number : "))

    Ret = Factor(Value)

    print("Factors of",Value,"are : ")

    for i in Ret:
        print(i)

if __name__ == "__main__":
    main()