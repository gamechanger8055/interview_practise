# OCC allows transactions to proceed without locking resources initially, checking for conflicts only during commit time.

import threading

class OCC:
    def __init__(self):
        self.data={}
        self.lock=threading.Lock()

    def read_data(self,key):
        with self.lock:
            return self.data[key]

    def write_data(self,key,value):
        with self.lock:
            if not self.data.get(key):
                self.data[key] = value
                print(f"Updated data: {self.data}")
                return True
            return False

resource = OCC()

def updater():
    for i in range(3):
        updated = resource.write_data('key', f'value_{i}')
        if not updated:
            print("Conflict detected, retrying...\n")


threads = []
for _ in range(3):
    t = threading.Thread(target=updater)
    threads.append(t)
    t.start()

for t in threads:
    t.join()