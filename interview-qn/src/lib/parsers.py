from abc import ABC

class BaseLogParser(ABC):
 def __init__(self, raw_log_data):
   self.raw_log_data = raw_log_data

 def is_eligible(self):
   pass
 
 def get_parsed_value(self):
   pass

