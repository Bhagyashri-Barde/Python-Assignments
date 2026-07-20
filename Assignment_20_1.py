'''
Program - Design Python Application 
Create 2 Threads Seprately 
1) Even Thread - Should Display First 10 Even Numbers

2) Odd Thread - Should Display First 10 Odd Numbers

Both Threads should execute independantly using threading Module
Ensure proper Thread creation and execution

'''
import threading

def Even():
    print("Even Numbers : ")

    for no in range(2,(10 * 2 + 1),2):

        print(no)

def Odd():
    print("Odd Numbers : ")

    for no in range(1,(10 * 2 + 1),2):

        print(no)

def main():
    
    t1 = threading.Thread(target=Even)

    t2 = threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
