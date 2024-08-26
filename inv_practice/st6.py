class Invoice:
    def __init__(self,timestamp,name,amount):
        self.timestamp=timestamp
        self.name=name
        self.amount=amount

    def __str__(self):
        return f'{{"invoice_time": {self.timestamp}, "name": "{self.name}", "amount": {self.amount}}}'

class ScheduledMessage:
    def __init__(self,timestamp,schedule,invoice:Invoice):
        self.timestamp=timestamp
        self.schedule=schedule
        self.invoice=invoice

    def __str__(self):
        return f'{self.timestamp}: [{self.schedule}] Invoice for {self.invoice.name} for {self.invoice.amount} dollars'


class Invoicer:
    def __init__(self):
        self.send_schedule = {
            -10: "Upcoming",
            0: "New",
            20: "Reminder",
            30: "Due"
        }
        self.invoices = {}

    def add_invoice(self,timestamp,name,amount):
        self.invoices[timestamp]=Invoice(timestamp,name,amount)

    def output(self):
        res=[]
        message_list=[]

        for timestamp in self.invoices:
            for time in self.send_schedule:
                scheduled_time=time+timestamp
                message = ScheduledMessage(scheduled_time, self.send_schedule[time], self.invoices[timestamp])
                message_list.append(message)

        message_list.sort(key=lambda m:m.timestamp)
        res.extend(str(message) for message in message_list)
        return res

    @staticmethod
    def run():
        invoicer = Invoicer()
        invoicer.add_invoice(0, "Alice", 200)
        invoicer.add_invoice(1, "Bob", 100)
        output = invoicer.output()
        for message in output:
            print(message)


if __name__ == "__main__":
    Invoicer.run()