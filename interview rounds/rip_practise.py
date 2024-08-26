import threading
from threading import Lock
class Kvstore:
    def __init__(self):
        self.store={}
        self.lock=Lock()
        self.transaction=[]

    def get(self,key):
        with self.lock:
            return self.store.get(key,None)

    def set(self,key,value):
        with self.lock:
            if self.transaction:
                self.transaction[-1].append(('set',key,self.store.get(key,None)))
            self.store[key]=value

    def delete(self,key):
        with self.lock:
            if self.transaction:
                self.transaction[-1].append(('delete',key,self.store.get(key,None)))
            if key in self.store:
                del self.store[key]

    def begin(self):
        with self.lock:
            self.transaction.append([])

    def rollback(self):
        with self.lock:
            if not self.transaction:
                raise ValueError("no transactions to rollback")
            last_transaction=self.transaction.pop()
            for action,key,value in last_transaction:
                if action=="set":
                    if not value:
                        del self.store[key]
                    else:
                        self.store[key]=value
                if action=="delete":
                    self.store[key] = value

    def commit(self):
        with self.lock:
            if not self.transaction:
                raise ValueError("no transactions to commit")
            self.transaction.pop()


def updatekvstore(store,key,value):
    store.set(key,value)
    print(f"Updated {key} to {value} \n")

kv_store=Kvstore()
threads=[]
for i in range(2):
    thread=threading.Thread(target=updatekvstore,args=(kv_store,"abc",i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

final_value = kv_store.get('abc')
print(f"Final value for 'concurrentKey': {final_value} \n")

kv_store.begin()

# Set a key-value pair
kv_store.set('key1', 'value1')
print(f"Set key1 to {kv_store.get('key1')}")

# Commit the transaction
kv_store.commit()
print(f"Final value of key1: {kv_store.get('key1')}")
print()

# Start another transaction
kv_store.begin()
kv_store.set('key1', 'value2')
print(f"Set key1 to {kv_store.get('key1')} (in transaction)")

# Rollback the transaction
kv_store.rollback()
print(f"After rollback, key1 is {kv_store.get('key1')}")
print()

# Error handling: Try to commit without an active transaction
try:
    kv_store.commit()  # This should raise an exception
except Exception as e:
    print(f"Error: {e}")
print()

# Error handling: Try to rollback without an active transaction
try:
    kv_store.rollback()  # This should raise an exception
except Exception as e:
    print(f"Error: {e}")
print()
