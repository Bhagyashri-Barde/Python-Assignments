# Program - lambda function using reduce() 
# accepts a list of numbers and returns 
# the product of all numbers

from functools import reduce

ProductOfNo = lambda No1, No2 : No1 * No2 
def main():
    Data = [1,2,3,4,5]

    print(f"List is : {Data}")

    Ret = reduce(ProductOfNo,Data)

    print(f"Product Of Numbers : {Ret}")

if __name__ == "__main__":
    main()


