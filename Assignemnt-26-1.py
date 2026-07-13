'''
Program - implement Class named Demo with following Specification
1) Should Conatin 2 instance variables - no1 ,no2
2) Should Conatin 1 class variables - Value
3) Define a constructor (__init__) - accept 2 parameters and initialize instance variable
4) Implement 2 instance Methods - 
            i) Fun() - Displays the Value of instance variables no1,no2
            ii) Gun() - Displays the Value of instance variables no1,no2
5) Create 2 Objects of Demo class - 
            i) obj1 = Demo(11,21)
            ii) obj2 = Demo(51,101)
6) Call instance method in given sequence -
            1)obj1.Fun()    2)obj2.Fun() 
            3)obj1.Gun()    4)obj2.Gun()

'''

class Demo():
    # Class Variable
    Value = 20     

    #Constructor                               
    def __init__(self,A,B):

        # Instance Variable
        self.no1 = A                             
        self.no2 = B

    # Instance Method
    def Fun(self):
        print()
        print("Inside Demo Fun...")
        print("Class Variable Value : ",Demo.Value)
        print("Value of No1 : ",self.no1)
        print("Value of No2 : ",self.no2)

     # Instance Method
    def Gun(self):
        print()
        print("Inside Demo Gun...")
        print("Class Variable Value : ",Demo.Value)
        print("Value of No1 : ",self.no1)
        print("Value of No2 : ",self.no2)

 # Object Creation
obj1 = Demo(11,21)
obj2 = Demo(51,101)

# Instance Method Call
obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()
