from abc import ABC
from typing import List

from src.lib.clients import BaseLogClient, ProdLogClient
from src.lib.entities import ActivityLog, EntityType, ActivityType, Attribute


class ActivityLogIngester(ABC):
 def __init__(self, client: BaseLogClient, **kwargs):
   self.client = client

 def map_activity_type(self,activity_type_str):
     mapping = {
         "Add user": ActivityType.ADD,
         "Updated app": ActivityType.UPDATE,
         "Delete": ActivityType.DELETE
     }
     return mapping.get(activity_type_str, None)

 def infer_entity_type(self,activity_type_str):
     if "user" in activity_type_str.lower():
         return EntityType.USER
     elif "app" in activity_type_str.lower():
         return EntityType.APP
     else:
         return None

 def parse_attributes(self,attr_dict):
     if attr_dict is None:
         return []
     return [Attribute(attribute_name=k, attribute_value=v) for k, v in attr_dict.items()]

 def parse_activity_log(self,data):
     entity_type = self.infer_entity_type(data['activity_type'])
     entity_id = int(data['target_id'])
     activity_type = self.map_activity_type(data['activity_type'])
     latest_attributes = self.parse_attributes(data['new_value'])

     return ActivityLog(
         entity_type=entity_type,
         entity_id=entity_id,
         activity_type=activity_type,
         latest_attributes=latest_attributes
     )

 def parse_data(self) -> List[ActivityLog]:
  activity_logs=[]
  responses=self.client.get_log_data()
  for response in responses:
    activity_log=self.parse_activity_log(response)
    activity_logs.append(activity_log)

  return activity_logs





if __name__ == "__main__":
  credentials="639aeee1d51415019744ebe0"
  client = ProdLogClient(credentials=credentials)
  #print(client.get_log_data())
  ingester = ActivityLogIngester(client=client)

  activity_logs = ingester.parse_data()
  #print(activity_logs)
  assert activity_logs is not None

  user_activities = [
    activity_log for activity_log in activity_logs if activity_log.entity_type == EntityType.USER and activity_log.activity_type == ActivityType.ADD
  ]

  assert len(user_activities) > 0

  for log in activity_logs:
    print(str(log))
