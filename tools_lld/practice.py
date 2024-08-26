# rate limiter:
import threading
import time
from collections import defaultdict, deque
from enum import Enum
import random


class RateLimiter:
    def __init__(self,rate,per):
        self.rate=rate
        self.per=per
        self.allowances={}
        self.lock=threading.Lock()

    def allow(self,key):
        current=time.time()
        with self.lock:
            if key not in self.allowances:
                self.allowances[key]=(self.rate,current)
            curr_token,last_time=self.allowances[key]
            elapsed_time=current-last_time
            curr_token=min(self.rate,curr_token+(elapsed_time*self.rate/self.per))
            if curr_token<1:
                self.allowances[key] = (curr_token, current)
                return False
            else:
                self.allowances[key] = (curr_token-1, current)
                return True


class Publisher:
    def __init__(self):
        self.subscribers=defaultdict(list)

    def subscribe(self,subscriber,topic):
        self.subscribers[topic].append(subscriber)

    def publish(self,message,topic):
        if topic in self.subscribers:
            for subscriber in self.subscribers[topic]:
                subscriber.event.set()
                subscriber.message=message

class Subscriber:
    def __init__(self,name):
        self.name=name
        self.message=None
        self.event=threading.Event()

    def receive(self):
        self.event.wait()
        print(f'{self.name} {self.message}')
        self.event.clear()

def rate_limiter_main():
    rate=5
    per=10
    key='user123'
    rate_limiter=RateLimiter(rate,per)
    for _ in range(10):
        if rate_limiter.allow(key):
            print("allowed")
        else:
            print("Rate limit exceeded")
        time.sleep(1)

def pubsub_main():
    publisher = Publisher()

    subscriber_1 = Subscriber("Subscriber 1")
    subscriber_2 = Subscriber("Subscriber 2")
    subscriber_3 = Subscriber("Subscriber 3")

    publisher.subscribe(subscriber_1, "sports")
    publisher.subscribe(subscriber_2, "entertainment")
    publisher.subscribe(subscriber_3, "sports")

    publisher.publish("Soccer match result", "sports")
    subscriber_1.receive()

class CircuitBreakerState(Enum):
    CLOSED = 1
    OPEN = 2
    HALF_OPEN = 3

class CircuitBreaker:
    def __init__(self,half_open_success_threshold,open_timeout,failure_threshold):
        self.half_open_success_threshold=half_open_success_threshold
        self.open_timeout=open_timeout
        self.failure_threshold=failure_threshold
        self.success_count=0
        self.failure_count=0
        self.last_failure_time=None
        self.current_state=CircuitBreakerState.CLOSED

    def record_success(self):
        if self.current_state==CircuitBreakerState.HALF_OPEN:
            self.success_count+=1
            if self.success_count>=self.half_open_success_threshold:
                self.transistion_to_closed()

    def record_failure(self):
        if self.current_state == CircuitBreakerState.CLOSED:
            self.failure_count+=1
            if self.failure_count>=self.failure_threshold:
                self.transistion_to_half_open()
        elif self.current_state==CircuitBreakerState.HALF_OPEN:
            self.transistion_to_open()

    def allow_requests(self):
        if self.current_state==CircuitBreakerState.CLOSED:
            return True
        elif self.current_state==CircuitBreakerState.HALF_OPEN:
            return True
        else:
            if time.time()-self.last_failure_time>=self.open_timeout:
                self.transistion_to_half_open()
                return True
            return False



    def get_state(self):
        return self.current_state

    def transistion_to_half_open(self):
        self.current_state = CircuitBreakerState.HALF_OPEN
        self.success_count = 0

    def transistion_to_open(self):
        self.current_state=CircuitBreakerState.OPEN
        self.success_count=0
        self.failure_count=0
        self.last_failure_time=time.time()

    def transistion_to_closed(self):
        self.success_count=0
        self.failure_count=0
        self.current_state=CircuitBreakerState.CLOSED




class Service:
    def __init__(self,circuit_breaker:CircuitBreaker):
        self.circuit_breaker=circuit_breaker

    def run(self):
        if self.circuit_breaker.allow_requests():
            try:
                #call service
                self.external_service_call()
                self.circuit_breaker.record_success()
            except Exception as e:
                self.circuit_breaker.record_failure()
                print(f"Service call failed: {e}")
            else:
                # Fallback logic when the circuit is open
                print("Circuit breaker is open. Executing fallback.")

    def external_service_call(self):
        #stimulate service call
        if random.random()<0.5:
            raise Exception("Service call failed")

def circuit_breaker_main():
    circuit_breaker = CircuitBreaker(failure_threshold=3, open_timeout=10, half_open_success_threshold=2)
    service = Service(circuit_breaker)

    for i in range(20):
        service.run()
        time.sleep(0.5)

class TrieNode:
    def __init__(self):
        self.children={}
        self.is_file=False
        self.content=""

class FileSystem:
    def __init__(self):
        self.root=TrieNode()

    def ls(self,path):
        curr_node = self.find(path)
        if not curr_node:
            return []
        if curr_node.is_file:
            return [path.split('/')[-1]]
        return list(curr_node.children.keys())


    def find(self,path):
        curr=self.root
        if path=="/":
            return curr
        path_list=path.split('/')[1:]
        for paths in path_list:
            if paths not in curr.children:
                return
            curr=curr.children[paths]
        return curr

    def mkdir(self,path):
        curr = self.root
        if path == "/":
            return curr
        path_list = path.split('/')[1:]
        for paths in path_list:
            if paths not in curr.children:
                curr.children[paths]=TrieNode()
            curr = curr.children[paths]

    def add_content_to_file(self,path,content):
        curr=self.root
        parts=path.split('/')[1:]
        for part in parts[:-1]: #removing last
            curr=curr.children.setdefault(part,TrieNode())
        curr = curr.children.setdefault(parts[-1], TrieNode())
        curr.is_file=True
        curr.content+=content


    def read_content_from_file(self,path):
        curr_node=self.find(path)
        if curr_node and curr_node.is_file:
            return curr_node.content
        return ""

def file_content_main():
    fs = FileSystem()
    fs.mkdir("/a/b/c")
    fs.add_content_to_file("/a/b/c/d", "hello")
    print(fs.read_content_from_file("/a/b/c/d"))  # Output: hello
    print(fs.ls("/a/b"))  # Output: ['c']

class LFU:
    def __init__(self,capacity):
        self.capacity=capacity
        self.key_value={}
        self.key_freq={}
        self.freq_key_deque=defaultdict(deque)
        self.min_freq=0

    def update_freq(self,key):
        freq=self.key_freq[key]
        self.key_freq[key]+=1
        self.freq_key_deque[freq].remove(key)

        if not self.freq_key_deque[freq]:
            del self.freq_key_deque[freq]
            if self.min_freq==freq:
                self.min_freq+=1

        self.freq_key_deque[freq+1].append(key)

    def get(self,key):
        if key in self.key_value:
            self.update_freq(key)
            return self.key_value[key]
        return -1

    def put(self,key,value):
        if key in self.key_value:
            self.update_freq(key)
            self.key_value[key]=value
        else:
            if len(self.key_value)>=self.capacity:
                evict_key=self.freq_key_deque[self.min_freq].popleft()
                del self.key_value[evict_key]
                del self.key_freq[evict_key]

            self.key_value[key] = value
            self.key_freq[key]=1
            self.freq_key_deque[1].append(key)
            self.min_freq=1


def lfu_main():
    lfu = LFU(2)
    lfu.put(1, 1)  # cache=[1,_], cnt(1)=1
    lfu.put(2, 2)  # cache=[2,1], cnt(2)=1, cnt(1)=1
    print(lfu.get(1))  # return 1
    lfu.put(3, 3)  # 2 is the LFU key, invalidate 2, cache=[3,1], cnt(3)=1, cnt(1)=2
    print(lfu.get(2))  # return -1 (not found)
    print(lfu.get(3))  # return 3
    lfu.put(4, 4)  # Both 1 and 3 have the same frequency, but 1 is LRU, invalidate 1, cache=[4,3], cnt(4)=1, cnt(3)=2
    print(lfu.get(1))  # return -1 (not found)
    print(lfu.get(3))  # return 3
    print(lfu.get(4))  # return 4

rate_limiter_main()
print()
pubsub_main()
print()
circuit_breaker_main()
print()
file_content_main()
print()
lfu_main()
print()