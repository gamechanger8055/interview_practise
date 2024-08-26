class Server:
    def __init__(self,id,address):
        self.id=id
        self.address=address
        self.connection=0

class LoadBalancer:
    def __init__(self):
        self.servers=[]
        self.index=0

    def add_server(self,server):
        self.servers.append(server)

    def get_server(self):
        server=self.servers[self.index]
        self.index=(self.index+1)%len(self.servers)
        return server

lb = LoadBalancer()
lb.add_server(Server(1, "192.168.1.1"))
lb.add_server(Server(2, "192.168.1.2"))

for _ in range(4):
    server = lb.get_server()
    print(server.address)
