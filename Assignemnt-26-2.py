'''
Program - implement Class named Circle with following Requirments
1) Should Conatin 3 instance variables - Radius,Area,Circumference
2) Should Conatin 1 class variables - PI initialized to 3.14
3) Define a constructor (__init__) - Initialized all instance variables to 0.0
4) Implement the following instance Methods - 
            i) Accept() - Accept Radius of circle from user
            ii) CalculateArea() - Calculate Area of the circle and store it in Area variable
            iii) CalculateCircumference() - Calculate circumference of circle and store it in Circumference variable 
            iv) Display() - Display the value of Radius, Area and Circumference
5) Create multiple Objects of Circle class and invoke all instance methods for each object

'''

class Circle():
    # Class Variable
    PI = 3.14   

    #Constructor                               
    def __init__(self):

        # Instance Variable
        self.Radius = 0.0                           
        self.Area = 0.0
        self.Circumference = 0.0
        
    # --- Start Instance Methods ---

    def Accept(self):
        print()
        radius = int(input("Enter Radius : "))
        self.Radius = radius
        
    def CalculateArea(self):
        
        # Area of Circle = πr2
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):

        #Circumference of Circle = 2πr
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print()
        print(f"Radius of Circle is:{self.Radius:.2f}")
        print(f"Area of Circle is: {self.Area:.2f}")
        print(f"Circumference of Circle is: {self.Circumference:.2f}")
    
    # --- End of Instance Methods ---

 # Object Creation
cObj1 = Circle()
cObj2 = Circle()
cObj3 = Circle()

# Instance Method Call
cObj1.Accept()
cObj1.CalculateArea()
cObj1.CalculateCircumference()
cObj1.Display()

cObj2.Accept()
cObj2.CalculateArea()
cObj2.CalculateCircumference()
cObj2.Display()

cObj3.Accept()
cObj3.CalculateArea()
cObj3.CalculateCircumference()
cObj3.Display()



