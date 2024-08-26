'''
Row-level locks are commonly used in databases to lock specific rows rather than entire tables.
'''
import threading


class RowLockingDatabase:
    def __init__(self):
        self.locks = {}
        self.data = {}

    def read_row(self, row_id):
        with self.locks.setdefault(row_id, threading.Lock()):
            with self.locks[row_id]:
                return self.data.get(row_id)

    def write_row(self, row_id, value):
        with self.locks.setdefault(row_id, threading.Lock()):
            with self.locks[row_id]:
                self.data[row_id] = value
                print(f"Updated row {row_id}: {self.data[row_id]}")


db = RowLockingDatabase()


def reader(row_id):
    value = db.read_row(row_id)
    print(f"Reader got value for row {row_id}: {value}")


def writer(row_id, value):
    db.write_row(row_id, value)


threads = []
for i in range(3):
    t = threading.Thread(target=reader, args=(f'row_{i}',))
    threads.append(t)
    t.start()

for i in range(2):
    t = threading.Thread(target=writer, args=(f'row_{i}', f'new_value_{i}'))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
