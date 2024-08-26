'''
Exclusive locks ensure that only one transaction can modify data at a time, preventing other transactions from reading
 or writing concurrently.
'''

import threading

class ExclusiveResource:
    def __init__(self):
        self.data={}
        self.lock=threading.Lock()

    def update_data(self,key,value):
        with self.lock:
            self.data[key]=value


resource = ExclusiveResource()

def updater():
    for i in range(3):
        resource.update_data('key', f'value_{i}')

threads = []
for _ in range(3):
    t = threading.Thread(target=updater)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
