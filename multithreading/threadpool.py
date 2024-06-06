from concurrent.futures import ThreadPoolExecutor
import time


def task(message):
    return f'Task executed with message : {message}'

def cpu_bound_task(n):
    result = sum(i ** 2 for i in range(n))
    return result

def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(cpu_bound_task, 1000000) for _ in range(5)]
        results = [future.result() for future in futures]
        print("Results:", results)

start_time = time.time()
main()
print("Execution time:", time.time() - start_time, "seconds")

start_time = time.time()
cpu_bound_task(1000000)
print("Execution time without concurrency:", time.time() - start_time, "seconds")