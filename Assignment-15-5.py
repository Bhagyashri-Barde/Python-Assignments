# Program - lambda function using reduce() 
# accepts a list of numbers and returns 
# the maximum elemnt

from functools import reduce

Max = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
    Data = [89,56,39,432,130]
    
    print(f"List is : {Data}")

    Ret = reduce(Max,Data)

    print(f"Maximum Element is: {Ret}")

if __name__ == "__main__":
    main()


