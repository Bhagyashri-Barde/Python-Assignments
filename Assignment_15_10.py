# Program - lambda function using filter() 
# accepts a list of numbers and returns 
# the count of even numbers
Even = lambda No : (No % 2 == 0) 

def main():
    Data = [8,83,9,21,48,96,63,18,65,20]

    print(f"List is : {Data}")

    Ret = len(list(filter(Even,Data)))

    print(f"Count of Even Numbers : {Ret}")

if __name__ == "__main__":
    main()


