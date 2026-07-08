'''
Program - Design Python Application 
Create 2 Threads  
1) EvenFactor Thread - i) Should identify all Even factors of given number
                       ii) Calculate and disply sum of Even factors

2) OddFactor Thread - i) Should identify all Odd factors of given number
                      ii) Calculate and disply sum of Odd factors

Both threads should accept one integer number as parameter
After both threads complete execution the main thread should dispaly the message
"Exit From Main"

'''
import threading

def EvenFactor(No):
    Sum = 0

    print("Even Factors : ")

    for i in range(2,No+1):
        
        if No % i == 0 and i % 2 == 0:
                
                print(i)

                Sum = Sum + i

    print("Summetion of Even Factors :",Sum)

def OddFactor(No):
    Sum = 0

    print("Odd Factors : ")

    for i in range(1,No+1):
        
        if No % i == 0 and i % 2 != 0:

            print(i)

            Sum = Sum + i
            
    print("Summetion of Odd Factors :",Sum)

def main():
    
    No =int(input("Enter Number : "))

    t1 = threading.Thread(target=EvenFactor,args=(No,))

    t2 = threading.Thread(target=OddFactor,args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit From Main")

if __name__ == "__main__":
    main()
