#locks the entire table

import threading

class TableLock:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()

    def update_table(self,key,value):
        with self.lock:
            for key in self.data:
                self.data[key]=value
            print(f"Updated entire table: {self.data}")

table = TableLock()

def updater():
    for i in range(3):
        table.update_table('key', f'value_{i}')

# Multiple threads trying to update the table concurrently
threads = []
for _ in range(3):
    t = threading.Thread(target=updater)
    threads.append(t)
    t.start()

for t in threads:
    t.join()