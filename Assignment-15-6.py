# Program - lambda function using reduce() 
# accepts a list of numbers and returns 
# the minimum elemnt

from functools import reduce

Min = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    Data = [89,56,11,39,432,130]
    
    print(f"List is : {Data}")
    
    Ret = reduce(Min,Data)

    print(f"Minimum Element is: {Ret}")

if __name__ == "__main__":
    main()


