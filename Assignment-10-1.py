# Program - Accept 1 Number
# Prints Multiplication Table of that number

print("-------------------------------------")
print("-------- MultiPlication Table -------")
print("-------------------------------------")

def MultiplicationTable(No):

    for i in range(1,11):
        print(No * i)

def main():

    Value = int(input("Enter Your Number : "))

    MultiplicationTable(Value)

if __name__ == "__main__":
    main()
