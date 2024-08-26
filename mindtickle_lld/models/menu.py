class Menu:
    def __init__(self):
        self.items={}
        self.ctr=0

    def add_item(self,item):
        self.items[self.ctr]=item