from collections import defaultdict, deque


class LFUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.min_freq=0
        self.key_to_value={}
        self.key_to_freq={}
        self.freq_to_key=defaultdict(deque)

    def _update_freq(self,key):
        freq=self.key_to_freq[key]
        self.key_to_freq[key]+=1
        self.freq_to_key[freq].remove(key)

        if not self.freq_to_key[freq]:
            del self.freq_to_key[freq]
            if self.min_freq==freq:
                self.min_freq+=1

        self.freq_to_key[freq+1].append(key)


    def get(self,key):
        if key in self.key_to_value:
            self._update_freq(key)
            return self.key_to_value[key]
        return -1

    def put(self,key,value):
        if key in self.key_to_value:
            self._update_freq(key)
            self.key_to_value[key]=value
        else:
            if len(self.key_to_value)==self.capacity:
                evict_key=self.freq_to_key[self.min_freq].popleft()
                del self.key_to_freq[evict_key]
                del self.key_to_value[evict_key]

            self.key_to_value[key]=value
            self.key_to_freq[key]=1
            self.freq_to_key[1].append(key)
            self.min_freq=1

lfu = LFUCache(2)
lfu.put(1, 1)   # cache=[1,_], cnt(1)=1
lfu.put(2, 2)   # cache=[2,1], cnt(2)=1, cnt(1)=1
print(lfu.get(1))  # return 1
lfu.put(3, 3)   # 2 is the LFU key, invalidate 2, cache=[3,1], cnt(3)=1, cnt(1)=2
print(lfu.get(2))  # return -1 (not found)
print(lfu.get(3))  # return 3
lfu.put(4, 4)   # Both 1 and 3 have the same frequency, but 1 is LRU, invalidate 1, cache=[4,3], cnt(4)=1, cnt(3)=2
print(lfu.get(1))  # return -1 (not found)
print(lfu.get(3))  # return 3
print(lfu.get(4))  # return 4



