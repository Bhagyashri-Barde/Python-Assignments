# Program - lambda function using map() 
# accepts a list of numbers and returns 
# a list of squares of each number

Square = lambda No : No * No

def main():
    Data = [2,4,6,8,10]

    print(f"List is : {Data}")

    Ret = list(map(Square,Data))

    print(f"Result is : {Ret}")

if __name__ == "__main__":
    main()