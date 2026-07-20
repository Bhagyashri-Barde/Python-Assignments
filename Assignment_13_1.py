# Program - Accept Length and Width of Rectangle and Prints Area

from Area import Rectangle

print("-----------------------------")
print("----- Area of Rectangle -----")
print("-----------------------------")

def main():
    Length = int(input("Enter Length : "))

    Width = int(input("Enter Width : "))

    Ret = Rectangle(Length,Width)

    print("Area of Rectangle is: ",Ret)
    
if __name__ == "__main__":
    main()