'''
Program - Design Python Application 
Create 2 Threads
1) Thread1 - Should display numbers from 1 to 50

2) Thread2 - Should display numbers from 50 to 1 in reverse order

Ensure That - Thread2 starts execution only after Thread1 has completed
Use appropriate thread synchronization

'''
import threading

def Thread1():
   print("Numbers : ")

   for i in range(1,51):
       
       print(i)

def Thread2():
    print("Reverse Order : ")

    for i in range(50,0,-1):
       
       print(i)

def main():
   
    t1 = threading.Thread(target=Thread1)

    t2 = threading.Thread(target=Thread2)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
