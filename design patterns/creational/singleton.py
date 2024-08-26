'''
Singleton: class ensures that it has one instance and provide global point of access to it.

1. Eager initialization: creates instance of singleton class at the time of class loading.
2. Lazy initialization: delays creation of singleton instance until its needed.
3. A synchronized method ensures thread safety by locking the method,
   preventing multiple threads from creating multiple instances simultaneously.  -->> very costly

4. Double-checked locking reduces the overhead of acquiring a lock by first checking if the instance is already created,
   then acquiring the lock, and checking again before creating the instance.  -->> most useful


    Method explanation

    Eager Initialization: The instance is created at the time of class loading.
     This is straightforward but may lead to resource wastage if the instance is never used.

    Lazy Initialization: The instance is created only when it is needed. This saves resources but needs to handle thread
                safety in multithreaded environments.

    Synchronized Method: The get_instance method is locked to ensure only one thread can create the instance at a time.
        This is thread-safe but may reduce performance due to the overhead of acquiring the lock every time get_instance is called.

    Double-Checked Locking: Combines lazy initialization with reduced locking overhead by first checking
            if the instance is created before acquiring the lock, then checking again after acquiring the lock before
            creating the instance. This is both thread-safe and efficient.

'''


class SingletonEager:
    _instance = None

    class _SingletonEager:
        def __init__(self):
            self.value = "Eager Initialization"

    _instance = _SingletonEager()

    @staticmethod
    def get_instance():
        return SingletonEager._instance


# Usage
singleton1 = SingletonEager.get_instance()
singleton2 = SingletonEager.get_instance()
print(singleton1.value)
print(singleton1 is singleton2)


class SingletonLazy:
    _instance = None

    class _SingletonLazy:
        def __init__(self):
            self.value = "Lazy Initialization"

    @staticmethod
    def get_instance():
        if SingletonLazy._instance is None:
            SingletonLazy._instance = SingletonLazy._SingletonLazy()
        return SingletonLazy._instance


# Usage
singleton1 = SingletonLazy.get_instance()
singleton2 = SingletonLazy.get_instance()
print(singleton1.value)
print(singleton1 is singleton2)

import threading


class SingletonSynchronized:
    _instance = None
    _lock = threading.Lock()

    class _SingletonSynchronized:
        def __init__(self):
            self.value = "Synchronized Initialization"

    @staticmethod
    def get_instance():
        with SingletonSynchronized._lock:
            if SingletonSynchronized._instance is None:
                SingletonSynchronized._instance = SingletonSynchronized._SingletonSynchronized()
        return SingletonSynchronized._instance


# Usage
singleton1 = SingletonSynchronized.get_instance()
singleton2 = SingletonSynchronized.get_instance()
print(singleton1.value)
print(singleton1 is singleton2)

import threading


class SingletonDoubleChecked:
    _instance = None
    _lock = threading.Lock()

    class _SingletonDoubleChecked:
        def __init__(self):
            self.value = "Double-Checked Locking Initialization"

    @staticmethod
    def get_instance():
        if SingletonDoubleChecked._instance is None:
            with SingletonDoubleChecked._lock:
                if SingletonDoubleChecked._instance is None:
                    SingletonDoubleChecked._instance = SingletonDoubleChecked._SingletonDoubleChecked()
        return SingletonDoubleChecked._instance


# Usage
singleton1 = SingletonDoubleChecked.get_instance()
singleton2 = SingletonDoubleChecked.get_instance()
print(singleton1.value)
print(singleton1 is singleton2)
