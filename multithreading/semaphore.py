import threading

semaphore = threading.Semaphore(value=2)  # Allow two threads at a time
result = []

def process_data(data,pq):
    with semaphore:
        result.append(data.upper()+pq)

# Create multiple threads to process data concurrently
threads = []
for i in range(5):
    thread = threading.Thread(target=process_data, args=(f"data_{i}","efesdfc"))
    thread.daemon=True
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Processed data:", result)
