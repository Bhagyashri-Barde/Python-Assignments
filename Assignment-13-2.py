# Program - Accept Radius of Circle and Prints Area

print("-----------------------------")
print("----- Area of Circle -----")
print("-----------------------------")
from Area import Circle

def main():
    Radius = int(input("Enter Radius : "))

    Ret = Circle(Radius)

    print("Area of Circle is: ",Ret)
    
if __name__ == "__main__":
    main()