import time,threading
class TokenBucket:
    def __init__(self,rate,capacity):
        self.rate=rate
        self.capacity=capacity
        self.tokens=capacity # no request
        self.last_refill_time=time.time()
        self.lock=threading.Lock()

    def is_allowed(self):
        with self.lock:
            now=time.time()
            time_elapsed=now-self.last_refill_time
            self.tokens=min(self.capacity,self.tokens+time_elapsed*self.rate)
            #print(now,self.last_refill_time,time_elapsed, self.tokens)
            self.last_refill_time=now
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            else:
                return False


rate_limiter = TokenBucket(rate=1, capacity=5)
for _ in range(10):
    print(rate_limiter.is_allowed())
    time.sleep(0.1)