'''
Program - Design Python Application 
Where multiple Threads update a shared variable
Use Lock to avoid race condition
each thread should increment Counter multiple times
Display the Final Value of the counter 
after all threads complete execution

'''
import threading 
lock = threading.Lock()
Counter = 0 

def IncrementCounter():
    global Counter

    for i in range(500):

        with lock:
            
            Counter = Counter + 1
def main():
   

   t1 = threading.Thread(target=IncrementCounter)

   t2 = threading.Thread(target=IncrementCounter)
   
   t3 = threading.Thread(target=IncrementCounter)
   
   t4 = threading.Thread(target=IncrementCounter)

   t1.start()
   t2.start()
   t3.start()
   t4.start()

   t1.join()
   t2.join()
   t3.join()
   t4.join()

   print("Final Counter Value :",Counter)

if __name__ == "__main__":
    main()