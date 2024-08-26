import threading

class PCCResource:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()

    def read_data(self, key):
        with self.lock:
            return self.data.get(key)

    def write_data(self, key, value):
        with self.lock:
            self.data[key] = value
            print(f"Updated data: {self.data}")

# Example usage
resource = PCCResource()

def updater():
    for i in range(3):
        with resource.lock:
            resource.write_data('key', f'value_{i}')

# Multiple threads trying to update concurrently
threads = []
for _ in range(3):
    t = threading.Thread(target=updater)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
