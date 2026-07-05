# Program - lambda function using filter() 
# accepts a list of numbers and returns 
# a list of numbers divisible by 3 and 5

ChkDivisible = lambda No : (No % 3 == 0 and No % 5 == 0)

def main():
    Data = [10,30,21,45,15,60]
    
    print(f"List is : {Data}")

    Ret = list(filter(ChkDivisible,Data))

    print(f"Result is : {Ret}")

if __name__ == "__main__":
    main()


