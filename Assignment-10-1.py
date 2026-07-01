# Program - Accept 1 Number
# Prints Multiplication Table of that number

print("-------------------------------------")
print("-------- MultiPlication Table -------")
print("-------------------------------------")

def MultiplicationTable(No):
    table = []

    for i in range(1,11):
        tblNo = No * i

        table.append(tblNo)

    return table

def main():

    Value = int(input("Enter Your Number : "))

    Ret = MultiplicationTable(Value)
    
    print("Table of",Value,"is : ")

    for i in Ret:
        print(i)

if __name__ == "__main__":
    main()
