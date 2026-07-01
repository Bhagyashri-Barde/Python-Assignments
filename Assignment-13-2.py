# Program - Accept Radius of Circle and Prints Area

from Area import Circle  

print("-----------------------------")
print("----- Area of Circle -----")
print("-----------------------------")

def main():
    Radius = int(input("Enter Radius : "))

    Ret = Circle(Radius)

    print("Area of Circle is: ",Ret)
    
if __name__ == "__main__":
    main()