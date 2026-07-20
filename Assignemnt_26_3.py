'''
Program - implement Class named Arithmatic with following Characteristics
1) Should Conatin 2 instance variables - Value1 ,Value2
2) Define a constructor (__init__) - Initialized all instance variables to 0
3) Implement the following instance Methods - 
            i) Accept() - Accepts values for Value1 and Value2 from user
            ii) Addition() - Returns the addition of Value1 and Value2
            iii) Subtraction() - Returns the subtraction of Value1 and Value2
            iii) Multiplication() - Returns the multiplication of Value1 and Value2
            iv) Division() - Returns the division of Value1 and Value2
                            (handle division by Zero)
4) Create multiple Objects of Arithmatic class and invoke all instance methods for each object

'''

class Arithmatic():

    #Constructor                               
    def __init__(self):

        # Instance Variable
        self.Value1 = 0                         
        self.Value2 = 0
        
    # --- Start Instance Methods ---
    
    def Accept(self):
        print()
        No1 = int(input("Enter Value1 : "))
        No2 = int(input("Enter Value2 : "))
        self.Value1 = No1
        self.Value2 = No2
        
    def Addition(self):
        print()
        Ans =  self.Value1 + self.Value2

        return Ans

    def Subtraction(self):
        Ans =  self.Value1 - self.Value2

        return Ans

    def Multiplication(self):
        Ans =  self.Value1 * self.Value2

        return Ans

    def Division(self):
       Ans = 0
       try:
            Ans = self.Value1 / self.Value2

            return Ans
        
       except ZeroDivisionError as zObj:

            print("Exception occure due to second oprand is zero :",zObj)

    # --- End of Instance Methods ---

 # Object Creation
aObj1 = Arithmatic()
aObj2 = Arithmatic()

# --Start Instance Method Call ----
aObj1.Accept()
addition  = aObj1.Addition()
subtraction = aObj1.Subtraction()
multiplication = aObj1.Multiplication()
division = aObj1.Division()

print(f"Addition is : {addition}")
print(f"Subtrction is : {subtraction}")
print(f"Multiplication is : {multiplication}")
if division != None :print(f"Division is : {division:.3f}")
else : print(f"Division is : {division:}")

aObj2.Accept()
print(f"Addition is : {aObj2.Addition()}")
print(f"Subtrction is : {aObj2.Subtraction()}")
print(f"Multiplication is : {aObj2.Multiplication()}")
print(f"Division is : {aObj2.Division()}")

# --End of Instance Method Call ----





