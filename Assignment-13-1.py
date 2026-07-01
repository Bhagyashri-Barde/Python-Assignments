# Program - Accept Length and Width of Rectangle and Prints Area

print("-----------------------------")
print("----- Area of Rectangle -----")
print("-----------------------------")
from Area import Rectangle

def main():
    Length = int(input("Enter Length : "))

    Width = int(input("Enter Width : "))

    Ret = Rectangle(Length,Width)

    print("Area of Rectangle is: ",Ret)
    
if __name__ == "__main__":
    main()