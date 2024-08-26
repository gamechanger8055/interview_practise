# Enter your code here. Read input from STDIN. Print output to STDOUT

class AccountPlan:
    def __init__(self, account_date, duration, plan, name):
        self.account_date = account_date
        self.duration = duration
        self.plan = plan
        self.name = name


class Scheduled:
    def __init__(self, scheduled_time, scheduled_template, invoice):
        self.scheduled_time = scheduled_time
        self.scheduled_template = scheduled_template
        self.invoice = invoice

    def __str__(self):
        return f'{self.scheduled_time} {self.scheduled_template} {self.invoice.plan} {self.invoice.name}'


class Notifier:
    def __init__(self):
        self.send_schedule = {
            0: "Welcome",
            -15: "Upcoming expiry",
            "end": "Expired"
        }
        self.user_invoices = {}

    def add_invoice(self, account_date, duration, plan, name):
        self.user_invoices[account_date] = AccountPlan(account_date, duration, plan, name)

    def send_emails(self):
        messages = []
        for dates in self.user_invoices:
            for time in self.send_schedule:
                if time=="end":
                    user_time=self.user_invoices[dates].duration
                elif time==-15:
                    user_time=self.user_invoices[dates].duration-15
                else:
                    user_time=time
                scheduled_time = dates + user_time
                scheduled = Scheduled(scheduled_time, self.send_schedule[time], self.user_invoices[dates])
                messages.append(scheduled)
        messages.sort(key=lambda x: x.scheduled_time)
        messages=[str(message) for message in messages]
        return messages


notifier=Notifier()
notifier.add_invoice(0,30,"silver","john")
notifier.add_invoice(1,15,"gold","alice")
print(notifier.send_emails())


#

