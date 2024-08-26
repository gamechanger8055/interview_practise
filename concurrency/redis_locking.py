import time
from redlock import RedLock,MultipleRedlockException
import redis

redis_client=redis.StrictRedis(host='localhost',port=6379,db=0)

def acquire_lock(lock_name,acquire_timeout=10,lock_timeout=60):
    lock_key=f'lock_{lock_name}'
    end_time=time.time()+acquire_timeout
    while time.time()<acquire_timeout:
        if redis_client.setnx(lock_key,"locked"):
            redis_client.expire(lock_key,lock_timeout)
            return True
        time.sleep(0.1)
    return False


def release_lock(lock_name):
    lock_key=f'lock_{lock_name}'
    redis_client.delete(lock_key)

lock_name = "event_update_lock"
if acquire_lock(lock_name):
    try:
        # Perform protected operation (e.g., update event)
        print("Lock acquired. Performing operation...")
        time.sleep(5)  # Simulate operation
        print("Operation completed.")
    finally:
        # Release the lock
        release_lock(lock_name)
else:
    print("Failed to acquire lock. Another process may be holding it.")

redis_servers = [
    {"host": "redis1.example.com", "port": 6379, "db": 0},
    {"host": "redis2.example.com", "port": 6379, "db": 0},
    {"host": "redis3.example.com", "port": 6379, "db": 0},
]
def distributed_lock(lock_name, timeout=10000):
    redlock=RedLock(lock_name,redis_servers)
    try:
        lock=redlock.lock(timeout=timeout)
    except MultipleRedlockException:
        print("Failed to acquire lock.")
    finally:
        if lock:
            redlock.unlock(lock)

lock_name = "calendar_event_lock"
distributed_lock(lock_name)


def optimistic_update_event(event_id, new_title, new_description):
    event_key = f"event:{event_id}"
    current_data=redis_client.hgetall(event_key)
    if not current_data:
        print(f"Event with ID {event_id} not found.")
        return

    current_version=int(current_data.get('version', 0))

    another_process_simulate_increment_version(event_id)

    if current_version != int(current_data.get('version', 0)):
        print(f"Event with ID {event_id} has been updated by another process. Please retry.")
        return

    updated_data = {
        'title': new_title,
        'description': new_description,
        'version': current_version + 1  # Increment version
    }

    redis_client.hset(event_key, updated_data)
    print(f"Event with ID {event_id} updated successfully.")

def another_process_simulate_increment_version(event_id):
    # Simulate another process incrementing the version
    event_key = f"event:{event_id}"
    redis_client.hincrby(event_key, 'version', 1)

optimistic_update_event(1, 'Updated Meeting', 'Discuss updated project')
