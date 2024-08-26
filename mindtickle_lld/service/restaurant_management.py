class RestaurantManagement:
    def __init__(self):
        self.tables=[None for _ in range(10)]

    def find_available_table(self):
        return self.tables.index(None)

    def reserve_table(self):
        first_available=self.find_available_table()
        self.tables[first_available]="Booked"

    def unreserve_table(self,table_id):
        self.tables[table_id]=None



