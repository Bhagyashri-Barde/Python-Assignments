# Program - Accept 1 number and checks whether 
# it is perfect number or not

from functools import reduce

Addition = lambda No1, No2 : No1 + No2

def ChkPerfectNumber(No):
    numList = list()
    Sum = 0

    for i in range(1,No):

        if(No % i == 0):
            numList.append(i)

    if(len(numList) == 0):
        return False
    else:
        Sum = reduce(Addition ,numList)

        if Sum == No:
            return True
        else:
            return False

def main():
    Value = int(input("Enter your number : "))

    Ret = ChkPerfectNumber(Value)

    if (Ret == True):
        print(Value,"is Perfect Number")
    else:
        print(Value,"is not Perfect Number")

if __name__ == "__main__":
    main()