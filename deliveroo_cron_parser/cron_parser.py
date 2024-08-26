import sys
from deliveroo_cron_parser.constants import *

class CronParser:
    def split_cron_parser(self,input):
        try:
            minute, hour, day, month, week, cmd = input.split(" ")
        except:
            raise Exception("Not enough parameters passed.")
        return '\n'.join([
            "minute        {}".format(self.define_string(minute, 'minute')),
            "hour          {}".format(self.define_string(hour, 'hour')),
            "day of month  {}".format(self.define_string(day, 'day')),
            "month         {}".format(self.define_string(month, 'month')),
            "day of week   {}".format(self.define_string(week, 'week')),
            "command       {}".format(cmd)
        ])

    def define_string(self,data,dataType):
        days=DAYS
        months=MONTHS
        values=VALUES

        if data=="*":
            return " ".join(map(str,values[dataType]))

        if data == "?":
            return "Not Specified"

        if "-" in data:
            value=days if dataType=="week" else "months"
            return self.handle_range(data,value,dataType)

        if '/' in data:
            return self.handle_intervals(data, values[dataType], dataType)

        if "," in data:
            if dataType in ["month", "week"]:
                val = days if dataType == "week" else months
                return self.handle_lists(data, values[dataType], dataType, val)
            else:
                return self.handle_lists(data, values[dataType], dataType)

        return data

    def handle_range(self,data,value,dataType):
        start,end=data.split("-")
        try:
            start, end=int(start),int(end)
        except ValueError:
            try:
                start, end = value.index(start), value.index(end)
                return " ".join(value[start:end + 1])
            except ValueError:
                raise Exception(f'{dataType} input combination is not valid. Please use either string or number syntax.')
        return " ".join(map(str, [i for i in range(start, end + 1)]))



    def handle_intervals(self,data, values, dataType):
        first,last=data.split("/")


    def handle_lists(data, values, dataType, sub_part=None):
        pass




    
if __name__=="__main__":
    cron_parser=CronParser()
    cron_parser.split_cron_parser(sys.argv[1])