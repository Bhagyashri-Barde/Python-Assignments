# Program - lambda function using filter() 
# accepts a list of numbers and returns 
# a list of Odd numbers

Odd = lambda No : (No % 2 != 0) 

def main():
    Data = [29,44,32,67,49,190]

    print(f"List is : {Data}") 

    Ret = list(filter(Odd,Data))

    print(f"Odd Numbers List : {Ret}")

if __name__ == "__main__":
    main()