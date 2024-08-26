class LRUCache:
    def __init__(self,capacity):
        self.mp={}
        self.l=[]
        self.capacity=capacity

    def get(self,key):
        if key in self.mp:
            self.l.remove(key)
            self.l.append(key)
            return self.mp[key]
        return -1

    def put(self,key,value):
        if key in self.mp:
            self.l.remove(key)
            self.l.append(key)
            self.mp[key]=value
        else:
            if len(self.mp)==self.capacity:
                lru=self.l.pop(0)
                del self.mp[lru]
            self.l.append(key)
            self.mp[key]=value

lru=LRUCache(2)
lru.put(1,1)
lru.put(2,2)
print(lru.get(1))
lru.put(3,3)
print(lru.get(2))
lru.put(4,4)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))