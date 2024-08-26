import time
import random
from enum import Enum

class CircuitBreakerStatus(Enum):
    CLOSED=1
    OPEN=2
    HALF_OPEN=3

class CircuitBreaker:
    def __init__(self, failure_threshold,open_timeout,half_open_success_threshold):
        self.state=CircuitBreakerStatus.CLOSED
        self.failure_threshold=failure_threshold
        self.open_timeout=open_timeout
        self.half_open_success_threshold=half_open_success_threshold
        self.failure_count=0
        self.success_count=0
        self.last_failure_time=None

    def allow_request(self):
        if self.state==CircuitBreakerStatus.CLOSED:
            return True
        elif self.state==CircuitBreakerStatus.OPEN:
            if time.time()-self.last_failure_time>=self.open_timeout:
                self._transition_to_half_open()
                return True
            return False
        elif self.state==CircuitBreakerStatus.HALF_OPEN:
            return True

    def _transition_to_half_open(self):
        self.state=CircuitBreakerStatus.HALF_OPEN
        self.success_count=0

    def _transition_to_closed(self):
        self.state=CircuitBreakerStatus.CLOSED
        self.failure_count=0
        self.success_count=0

    def _transition_to_open(self):
        self.state = CircuitBreakerStatus.OPEN
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time=time.time()

    def get_state(self):
        return self.state

    def record_success(self):
        if self.state==CircuitBreakerStatus.HALF_OPEN:
            self.success_count+=1
            if self.success_count>=self.half_open_success_threshold:
                self._transition_to_closed()

    def record_failure(self):
        if self.state == CircuitBreakerStatus.CLOSED:
            self.failure_count+=1
            if self.failure_count>=self.failure_threshold:
                self._transition_to_open()
        elif self.state == CircuitBreakerStatus.HALF_OPEN:
            self._transition_to_open()

class Service:
    def __init__(self,circuit_breaker:CircuitBreaker):
        self.circuit_breaker=circuit_breaker

    def call(self):
        if self.circuit_breaker.allow_request():
            try:
                #call external service
                self.external_service_call()
                self.circuit_breaker.record_success()
            except Exception as e:
                self.circuit_breaker.record_failure()
                # Handle the exception
                print(f"Service call failed: {e}")
            else:
                # Fallback logic when the circuit is open
                print("Circuit breaker is open. Executing fallback.")

    def external_service_call(self):
        #stimulate service call
        if random.random()<0.7:
            raise Exception("Service call failed")

if __name__ == "__main__":
    circuit_breaker = CircuitBreaker(failure_threshold=3, open_timeout=10, half_open_success_threshold=2)
    service = Service(circuit_breaker)

    for i in range(20):
        service.call()
        time.sleep(0.5)  # Wait between calls

