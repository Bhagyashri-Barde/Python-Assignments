'''
Program - implement a Class named BankAccount with following Requirements
1) Should Conatin 2 instance variables - Name(Account Holder Name) ,Amount (Account Balance)
2) Should Conatin 1 class variable -  ROI (Rate Of Interest) initialized to 10.5
3) Define a constructor (__init__) - accept Name and Initial Amount
4) Implement following instance Method - 
                i) Display() - Display Account Holder Name and Current Balance
                ii) Deposit() - Accept an amount from user and add its to the balance
                iii) Withdraw() - Accept an amount from user and subtract it from balance
                                (Withdrow allowd only if sufficient balance exist)
                iv) CalculateInterest() - (Amount * ROI) / 100
5) Create multiple objects and demonstrate all methods
'''

class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):

        self.Name = Name

        self.Amount = Amount

    def Display(self):
        
        print()
        print(f"Bank Account Holder Name : {self.Name}")
        print(f"Current Balance : {self.Amount}")

    def Deposit(self):

        amount = int(input("How many amount you want to Deposit : "))
        
        self.Amount = self.Amount + amount

    def Withdraw(self):

         amount = int(input("How many amount you want to Withdraw : ")) 
         
         if self.Amount < amount :
             
             print()
             print("Insufficient Balance")

         else:
             
             self.Amount = self.Amount - amount

    def CalculateInterest(self):

        interest = (self.Amount * BankAccount.ROI) / 100

        print()
        print("Interest is :",interest)
        
name = input("Enter Account Holder Name : ")
currentBalance = int(input("Enter Current Balance : "))

bObj1 = BankAccount(name,currentBalance)

bObj1.Display()
bObj1.Deposit()
bObj1.Display()
bObj1.Withdraw()
bObj1.Display()
bObj1.CalculateInterest()


bObj2 = BankAccount("Devansh Patil",25500)

bObj2.Display()
bObj2.Deposit()
bObj2.Display()
bObj2.Withdraw()
bObj2.Display()
bObj2.CalculateInterest()

