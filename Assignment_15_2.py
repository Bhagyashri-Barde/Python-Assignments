# Program - lambda function using filter() 
# accepts a list of numbers and returns 
# a list of Even numbers

Even = lambda No : (No % 2 == 0) 

def main():
    Data = [29,44,32,67,49,190]

    print(f"List is : {Data}")

    Ret = list(filter(Even,Data))

    print(f"Even Numbers List : {Ret}")

if __name__ == "__main__":
    main()