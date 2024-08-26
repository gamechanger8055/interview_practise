import random
import threading
class LoadBalancer:
    def __init__(self):
        self.servers=[]
        self.lock=threading.Lock()
        self.current_index=0

    def add_server(self,server):
        with self.lock:
            self.servers.append(server)

    def remove_server(self,server):
        with self.lock:
            self.servers.remove(server)

    def round_robin(self):
        #if a request comes the request goes to current server
        with self.lock:
            if not self.servers:
                return
            curr_server=self.servers[self.current_index]
            self.current_index=(self.current_index+1)%len(self.servers)
            return curr_server

    def least_connections(self,connections):
        with self.lock:
            if not self.servers:
                return
            # Initialize minimum connections and corresponding server
            min_connections = float('inf')
            min_server = None

            # Iterate over each server to find the one with the least connections
            for server in self.servers:
                current_connections = connections.get(server, 0)
                if current_connections < min_connections:
                    min_connections = current_connections
                    min_server = server

            return min_server

    def random_choice(self):
        with self.lock:
            if not self.servers:
                return
            return random.choice(self.servers)

lb = LoadBalancer()
lb.add_server('server1')
lb.add_server('server2')

connections = {'server1': 5, 'server2': 3}

print(lb.round_robin())  # Output: server1
print(lb.least_connections(connections))  # Output: server2
print(lb.random_choice())  # Output: server1 or server2 (random)



