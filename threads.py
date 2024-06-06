import threading
from threading import Thread
from time import sleep


print(threading.main_thread(),threading.currentThread().is_alive(),threading.current_thread().ident)
videos=['oops','constructor','destructor','file handling']

class MyThread(Thread):
    def __init__(self,val):
        print("constructor")
        self.kid=val
        Thread.__init__(self)

    def compression(self):
        print("video compression")

    def run(self):
        a=10
        b=20
        self.compression()
        if self.kid:
            print("kids suitable")
        for vid in videos:
            print("start upload...")
            sleep(1)
            print("bideo uploaded")
        self.temp=a+b

t3=MyThread(True)
t3.start()
sleep(10)
print(t3.temp)

for i in range(4):
    sleep(0.5)
    print("checking ciopyrughts")

#simple function
def display(n,msg):
    for i in range(n):
        print(msg)

t1=Thread(target=display,args=(3,"paytm kro!!"))
t2=Thread(target=display,kwargs={'n':8,"msg":"paytm band!!"})

t1.start()
t2.start()

#in case of class use its method in target.