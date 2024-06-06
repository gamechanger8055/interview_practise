import threading, time


def access_resource(lock):
    with lock:
        print(f"{threading.current_thread().name} is accessing the resource.")
        time.sleep(1)
        print(f"{threading.current_thread().name} finished accessing the resource.")


def main():
    lock = threading.Lock()
    #threads = []
    for i in range(5):
        thread = threading.Thread(target=access_resource, args=(lock,))
        thread.start()
        #threads.append(thread)

    # for thread in threads:
    #     thread.join()


main()
