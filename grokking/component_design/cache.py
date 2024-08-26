from collections import deque

class KeyValueStore:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}
        self.q=deque()

    def get(self,key):
        if key in self.cache:
            self.q.remove(key)
            self.q.appendleft(key)
            return self.cache[key]
        return -1

    def put(self,key,value):
        if key not in self.cache:
            if len(self.cache)>=self.capacity:
                lru=self.q.pop()
                del self.cache[lru]
            self.cache[key]=value
            self.q.appendleft(key)
        else:
            self.q.remove(key)
            self.cache[key] = value
            self.q.appendleft(key)

# Example usage
cache = KeyValueStore(2)

# Putting values into the cache
cache.put(1, 1)
cache.put(2, 2)

# Getting values
print(cache.get(1))  # returns 1

# Cache now holds (2, 2) and (1, 1) with (1, 1) being most recently used

# Adding another value should evict the least recently used (2, 2)
cache.put(3, 3)

print(cache.get(2))  # returns -1 (not found)

# Adding another value should evict the least recently used (1, 1)
cache.put(4, 4)

print(cache.get(1))  # returns -1 (not found)
print(cache.get(3))  # returns 3
print(cache.get(4))  # returns 4

