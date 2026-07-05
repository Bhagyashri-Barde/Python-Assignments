# Program - lambda function using filter() 
# accepts a list of strings and returns 
# a list of strings having length greater than 5

MaxLength = lambda name : len(name) > 5

def main():
    Data = ["Ram","Shyam","Krishna","Sai","Raghav"]

    print(f"List is : {Data}")

    Ret = list(filter(MaxLength,Data))

    print(f"Result is : {Ret}")

if __name__ == "__main__":
    main()


