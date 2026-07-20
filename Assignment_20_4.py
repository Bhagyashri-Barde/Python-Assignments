'''
Program - Design Python Application 
Create 3 Threads
1) Small Thread - Should count and display the number of lowercase characters

2) Capital Thread - Should count and display the number of lowercase characters

3) Digits Thread - Should count and display the number of Numeric digits
All threads should accept String as input
Each Thread Must also display

1) Thread ID      2) Thread Name

'''
import threading

def Small(name):
   print("Thread ID :",threading.get_ident())

   print("Thread Name :",threading.current_thread().name)
   
   Count = 0

   for ch in name:
       
       if ch.islower():
          
          Count = Count + 1

   print(f"No of LowerCase Characters in {name} is : {Count}")

def Capital(name):
    print("Thread ID :",threading.get_ident())

    print("Thread Name :",threading.current_thread().name)
    
    Count = 0

    for ch in name:
       
       if ch.isupper():
          
          Count = Count + 1

    print(f"No of UpperCase Characters in {name} is : {Count}")
    
   

def Digits(name):
     print("Thread ID :",threading.get_ident())
     
     print("Thread Name :",threading.current_thread().name)
     
     Count = 0

     for ch in name:
       
       if ch.isdigit():
          
          Count = Count + 1

     print(f"No ofdigits in {name} is : {Count}")
    

def main():
   
    name = input("Enter your String : ")

    t1 = threading.Thread(target=Small,args=(name,))

    t2 = threading.Thread(target=Capital,args=(name,))

    t3 = threading.Thread(target=Digits,args=(name,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
