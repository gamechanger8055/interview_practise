import threading
from collections import defaultdict
class Publisher:
    def __init__(self):
        self.subscribers=defaultdict(list)

    def subscribe(self,subscriber,topic):
        self.subscribers[topic].append(subscriber)

    def publish(self,message, topic):
        if topic in self.subscribers:
            for subscriber in self.subscribers[topic]:
                subscriber.event.set()
                subscriber.message=message


class Subscriber:
    def __init__(self,name):
        self.name=name
        self.event=threading.Event()
        self.message=None

    def receive(self):
        self.event.wait()
        print(f"{self.name} {self.message}")
        self.event.clear()


publisher = Publisher()

subscriber_1 = Subscriber("Subscriber 1")
subscriber_2 = Subscriber("Subscriber 2")
subscriber_3 = Subscriber("Subscriber 3")

publisher.subscribe(subscriber_1, "sports")
publisher.subscribe(subscriber_2, "entertainment")
publisher.subscribe(subscriber_3, "sports")

publisher.publish("Soccer match result", "sports")
subscriber_1.receive()