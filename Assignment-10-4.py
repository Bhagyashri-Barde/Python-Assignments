# Program - Accept 1 number and
# Prints All Even Numbers till that Number

print("-------------------------------------")
print("------------ Even Numbers -----------")
print("-------------------------------------")

def Even(No):

    print("Even Numbers Are : ")

    for i in range(1,No+1):

        if( i % 2 == 0 ):
            print(i)

def main():

    Value = int(input("Enter Your Number : "))

    Even(Value)

if __name__ == "__main__":
    main()