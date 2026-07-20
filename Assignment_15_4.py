# Program - lambda function using reduce() 
# accepts a list of numbers and returns 
# the addition of all elements

from functools import reduce

Sum = lambda No1, No2 : No1 + No2

def main():
    Data = [10,20,30,40,50]
    
    print(f"List is : {Data}")

    Ret = reduce(Sum,Data)

    print(f"Addition is : {Ret}")

if __name__ == "__main__":
    main()