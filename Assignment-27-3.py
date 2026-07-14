'''
Program - implement a Class named Numbers with following Specifications
1) Should Conatin 1 instance variables - Value
3) Define a constructor (__init__) - accepts number from user and initialize Value
4) Implement following instance Method - 
                i) ChkPrime() - Return True if number is Prime otherwise return False
                ii) ChkPerfect() - Return True if number is Perfect otherwise return False
                iii) Factors() - Display All Factors of the Number
                iv) SumFactors() - Return the sum of all factors
5) Create multiple objects and call all methods
'''

class Numbers:

    def __init__(self,Value):

        self.Value = Value

    def ChkPrime(self):

        Count = 0
        no = self.Value

        for i in range(1,no + 1):
             
             if no % i == 0:
                 
                 Count = Count + 1

        if Count == 2:

            return True
        
        else:

            return False


    def ChkPerfect(self):
        Sum = 0
        no = self.Value

        for i in range(1,no):

            if no % i == 0:

                Sum = Sum + i

        if no == Sum:

            return True
        
        else:

            return False

    def Factors(self):
        factorsList = list()

        no = self.Value

        for i in range(1,no + 1):

            if no % i == 0:

                factorsList.append(i)

        print(f"Factors of {no} are : {factorsList}")

    def SumFactors(self):
        Sum = 0
        no = self.Value

        for i in range(1,no + 1 ):

            if no % i == 0:

                Sum = Sum + i

        return Sum
print()
No1 = int(input("Enter Your Number : "))  
print()

nObj1 = Numbers(No1)

isPrime = nObj1.ChkPrime()

if isPrime: 
    print(f"{No1} is Prime Number")

else:

    print(f"{No1} is Not Prime Number")

isPerfect = nObj1.ChkPerfect()

if isPerfect: 

    print(f"{No1} is Perfect Number")

else:

    print(f"{No1} is Not Perfect Number")

nObj1.Factors()

total = nObj1.SumFactors()

print(f"Sum Of Factors of {No1} is : {total}")

print()

No2 = int(input("Enter Your Number :")) 

print()

nObj2 = Numbers(No2)

isPrime = nObj2.ChkPrime()

if isPrime: 

    print(f"{No2} is Prime Number")

else:

    print(f"{No2} is Not Prime Number")

isPerfect = nObj2.ChkPerfect()

if isPerfect: 

    print(f"{No2} is Perfect Number")

else:

    print(f"{No2} is Not Perfect Number")

nObj2.Factors()

total = nObj2.SumFactors()

print(f"Sum Of Factors of {No2} is : {total}")

print()

No3 = int(input("Enter Your Number : ")) 

print()

nObj3 = Numbers(No3)

isPrime = nObj3.ChkPrime()

if isPrime: 

    print(f"{No3} is Prime Number")

else:

    print(f"{No3} is Not Prime Number")

isPerfect = nObj3.ChkPerfect()

if isPerfect:
    
    print(f"{No3} is Perfect Number")

else:
    print(f"{No3} is Not Perfect Number")

nObj3.Factors()

total = nObj3.SumFactors()

print(f"Sum Of Factors of {No3} is : {total}")


