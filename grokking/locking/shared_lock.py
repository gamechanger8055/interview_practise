'''
In a shared lock scenario, multiple transactions can read data concurrently, but only one transaction can acquire an
 exclusive lock for writing.
'''

import threading

class SharedResource:
    def __init__(self):
        self.data={}
        self.lock=threading.Lock()

    def read_data(self,key):
        with self.lock:
            return self.data.get(key)

    def write_data(self,key,value):
        with self.lock:
            self.data[key]=value

#usage
resource=SharedResource()

def reader():
    value = resource.read_data('key')
    print(f"Reader got value: {value}")

def writer():
    resource.write_data('key', 'new_value')
    print("Writer updated value")

threads=[]
for _ in range(3):
    t=threading.Thread(target=reader)
    threads.append(t)
    t.start()

for _ in range(2):
    t = threading.Thread(target=writer)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

