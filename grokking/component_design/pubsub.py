from collections import defaultdict
import threading
from queue import Queue

'''
class Broker:
    def __init__(self):
        self.topics={}
        self.lock=threading.Lock()

    def create_topic(self,topic_name):
        with self.lock:
            self.topics[topic_name]=[]

    def produce(self,topic_name,message):
        with self.lock:
            if topic_name in self.topics:
                self.topics[topic_name].append(message)
            else:
                print(f"Topic {topic_name} does not exist")

    def subscribe(self,topic_name):
        if topic_name in self.topics:
            return Subscriber(self,topic_name)
        else:
            print(f"Topic {topic_name} does not exist")

class Subscriber:
    def __init__(self,broker,topic_name):
        self.broker=broker
        self.topic_name=topic_name
        self.offset=0

    def poll(self):
        if self.offset<len(self.broker.topics[self.topic_name]):
            message=self.broker.topics[self.topic_name][self.offset]
            self.offset+=1
            return message
        return

broker=Broker()
broker.create_topic("news")

broker.produce("news","breaking 1")
broker.produce("news","breaking 2")

consumer = broker.subscribe("news")
print(consumer.poll())  # Output: Breaking news 1
print(consumer.poll())  # Output: Breaking news 2

'''

class Publisher:
    def __init__(self):
        self.subscribers={}

    def subscribe(self,subscriber,topic):
        if topic not in self.subscribers:
            self.subscribers[topic]=[]
        self.subscribers[topic].append(subscriber)

    def publish(self,message,topic):
        if topic in self.subscribers:
            for subscriber in self.subscribers[topic]:
                subscriber.event.set()
                subscriber.message=message

class Subscribers:
    def __init__(self,name):
        self.name=name
        self.event=threading.Event()
        self.message=None

    def receive(self):
        self.event.wait()
        print(f"{self.name}" + "received message:"+f"{self.message}")
        self.event.clear()


publisher = Publisher()

subscriber_1 = Subscribers("Subscriber 1")
subscriber_2 = Subscribers("Subscriber 2")
subscriber_3 = Subscribers("Subscriber 3")

publisher.subscribe(subscriber_1, "sports")
publisher.subscribe(subscriber_2, "entertainment")
publisher.subscribe(subscriber_3, "sports")

publisher.publish("Soccer match result", "sports")
subscriber_1.receive()
