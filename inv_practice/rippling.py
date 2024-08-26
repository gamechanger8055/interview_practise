import threading
import time


#part 1:Design a K-V Store to support the following: getByKey, updateValueByKey, removeKey

class KVStore:
    def __init__(self):
        self.store={}

    def getByKey(self,key):
        return self.store.get(key,None)

    def updateValueByKey(self,key,value):
        self.store[key]=value

    def removeKey(self,key):
        if key in self.store:
            del self.store[key]

kvstore=KVStore()
kvstore.updateValueByKey(1,"abc")
print(kvstore.getByKey(2))
kvstore.removeKey(1)
print(kvstore.getByKey(1))

class KVStoreWithConcurrency:
    def __init__(self):
        self.store={}
        self.lock=threading.Lock()

    def getByKey(self,key):
        with self.lock:
            return self.store.get(key,None)

    def updateValueByKey(self,key,value):
        with self.lock:
            self.store[key]=value

    def removeKey(self,key):
        with self.lock:
            if key in self.store:
                del self.store[key]

kvcon=KVStoreWithConcurrency()

def update_store(store,key,value):
    store.updateValueByKey(key,value)
    print(f"Updated {key} to {value}")

threads=[]
for i in range(2):
    thread=threading.Thread(target=update_store,args=(kvcon,"concurrentKey",i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    #time.sleep(10)

final_value = kvcon.getByKey('concurrentKey')
print(f"Final value for 'concurrentKey': {final_value} \n")



class KVStoreWithConcurrencyAndTransaction:
    def __init__(self):
        self.store={}
        self.lock=threading.Lock()
        self.transactions=[]

    def getByKey(self,key):
        with self.lock:
            return self.store.get(key,None)

    def updateValueByKey(self,key,value):
        with self.lock:
            if self.transactions:
                self.transactions[-1].append(('set',key,self.store.get(key,None)))
            self.store[key]=value

    def removeKey(self,key):
        with self.lock:
            if self.transactions:
                self.transactions[-1].append(('delete',key,self.store.get(key,None)))
            if key in self.store:
                del self.store[key]

    def begin_transaction(self):
        with self.lock:
            self.transactions.append([])

    def rollback_transaction(self):
        with self.lock:
            if not self.transactions:
                raise ValueError("no transactions to rollback")
            last_transaction=self.transactions.pop()
            for action,key,value in last_transaction:
                if action=="set":
                    if not value:
                        del self.store[key]
                    else:
                        self.store[key]=value
                if action=="delete":
                    self.store[key]=value

    def commit_transaction(self):
        with self.lock:
            if not self.transactions:
                raise ValueError("no transactions to commit")
            self.transactions.pop()

def thread_safe_store(store):
    store.updateValueByKey(1,"abc")
    store.begin_transaction()
    store.updateValueByKey(1, "xyz")
    print(store.getByKey(1))
    store.rollback_transaction()
    print(store.getByKey(1))


kvtc=KVStoreWithConcurrencyAndTransaction()
threads=[]
for i in range(5):
    thread=threading.Thread(target=thread_safe_store,args=(kvtc,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

print("--------------elvish-----------",kvtc.getByKey(1))
kvtc.begin_transaction()
kvtc.updateValueByKey(1,"abc")
print(f"Set key1 to {kvtc.getByKey(1)}")
kvtc.commit_transaction()
print(f"Final value of key1: {kvtc.getByKey(1)}")
print()

print("Scenario 2: Nested transactions with rollback")
kvtc.begin_transaction()
kvtc.updateValueByKey('key1', 'value1')
kvtc.begin_transaction()
kvtc.updateValueByKey('key1', 'value2')
print(f"Set key1 to {kvtc.getByKey('key1')} (nested transaction)")
kvtc.rollback_transaction()  # Rollback the nested transaction
print(f"Rolled back nested transaction, key1 is now {kvtc.getByKey('key1')}")
kvtc.commit_transaction()  # Commit the outer transaction
print(f"Committed outer transaction, key1 is now {kvtc.getByKey('key1')}")
print()

print("Scenario 3: Multiple transactions with rollback")
kvtc.begin_transaction()
kvtc.updateValueByKey('key2', 'value1')
kvtc.begin_transaction()
kvtc.updateValueByKey('key1', 'value2')
print(f"Set key1 to {kvtc.getByKey('key1')} (nested transaction)")
kvtc.rollback_transaction()  # Rollback the nested transaction
print(f"Rolled back nested transaction, key1 is now {kvtc.getByKey('key1')}")
kvtc.commit_transaction()  # Commit the outer transaction
print(f"Committed outer transaction, key1 is now {kvtc.getByKey('key1')}")
print()

