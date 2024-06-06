import threading

def task():
    for i in range(5):
        print("hello")

t1=threading.Thread(target=task())
t2=threading.Thread(target=task())

t1.start()
print("heeeee")
t2.start()

#print("heeeee")
t1.join(timeout=1)
t2.join(timeout=1)