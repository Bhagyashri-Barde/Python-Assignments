def Addition(No1,No2):

    Sum = 0
    Sum = No1 + No2

    return Sum

def Subtraction(No1,No2):

    Subtact = 0
    Subtact = No1 - No2

    return Subtact

def Multiplication(No1,No2):

    Multiply = 0 
    Multiply = No1 * No2

    return Multiply

def Division(No1,No2):

    Div = 0

    if No2 == 0:
        
        return "Error : Division by zero not allowed..."
    else :

        Div = No1 / No2
        return Div
