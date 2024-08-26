'''
Design distributed locking via Redis

Implementing distributed locking using Redis is a common pattern in distributed systems where multiple nodes need to
 coordinate access to a shared resource to maintain consistency and prevent race conditions. Redis provides atomic
operations that are crucial for implementing distributed locking efficiently.

Requirements:
1. Lock Acquire- client should be able to acquire lock using redis
2. Lock release- client should be able to release lock when not needed
3. Safety- Ensure that locks are properly managed in case of network partirions ,failures and

'''

import redis
import uuid
import time


class RedisDistributedLock:
    def __init__(self,redis_host='localhost',redis_port=6379, lock_timeout=100):
        self.lock_timeout=lock_timeout
        self.redis_client=redis.StrictRedis(host=redis_host,port=redis_port,decode_responses=True)

    def acquire_lock(self,lock_name,owner_id):
        lock_value=owner_id or uuid.uuid4()

        # Trying to acquire the lock using SETNX command
        lock_key = f"lock:{lock_name}"
        lock_acquired=self.redis_client.set(name=lock_key,value=lock_value,nx=True,ex=self.lock_timeout)
        return lock_acquired

    def release_lock(self,lock_name,owner_id):
        lock_key = f"lock:{lock_name}"
        current_owner=self.redis_client.get(lock_key)
        if current_owner==owner_id:
            self.redis_client.delete(lock_key)
            return True
        return False

lock_manager=RedisDistributedLock()

resource_name = "resource123"
client_id = str(uuid.uuid4())
lock_acquired = lock_manager.acquire_lock(resource_name, client_id)
if lock_acquired:
    print(f"Lock acquired for resource '{resource_name}' by client '{client_id}'")
    # Do critical section work here...
    time.sleep(5)  # Simulate work being done in the critical section
    # Release lock
    released = lock_manager.release_lock(resource_name, client_id)
    if released:
        print(f"Lock released for resource '{resource_name}' by client '{client_id}'")
    else:
        print(f"Failed to release lock for resource '{resource_name}' by client '{client_id}'")
else:
    print(f"Failed to acquire lock for resource '{resource_name}' by client '{client_id}'")

