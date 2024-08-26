import time
import threading

class RateLimiter:
    def __init__(self,rate,per):
        self.rate=rate
        self.per=per
        self.allowances={}
        self.lock=threading.Lock()

    def allow(self,key):
        current_time=time.time()
        with self.lock:
            if key not in self.allowances:
                self.allowances[key]=(self.rate,current_time)
            tokens,last_time=self.allowances[key]
            elapsed_time=current_time-last_time
            tokens=min(self.rate,tokens+(elapsed_time*self.rate/self.per))
            if tokens<1:
                self.allowances[key]=(tokens,current_time)
                return False
            else:
                self.allowances[key] = (tokens - 1, current_time)
                return True

limiter = RateLimiter(rate=5, per=10) # RATE requests are allowed per PER seconds
key = 'user:123'
for _ in range(10):
    if limiter.allow(key):
        print("Allowed")
    else:
        print("Rate limit exceeded")
    time.sleep(1)