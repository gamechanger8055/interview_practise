import requests

from abc import ABC, abstractmethod
from typing import Dict, List


class BaseLogClient(ABC):
 base_url: str
 @abstractmethod
 def get_log_data(self) -> List[Dict]:
   """
   Calls the API to return activity logs
   Returns:
     {
       "activity_type": "Add user",
       "target_id": "1",
       "old_value": {"foo": "bar"},
       "new_value": {"foo": "bar2"},
       "change_timestamp": 1650333433,
     },
     {
       "activity_type": "Delete app",
       "target_id": "2",
       "old_value": {"foo": "bar"},
       "new_value": None,
       "change_timestamp": 1650333433,
     }
 
   """
   pass

class ProdLogClient(BaseLogClient):
  base_url="https://{}.mockapi.io/api/activity_logs"

  def __init__(self, credentials) -> None:
    self.base_url = self.base_url.format(credentials)

  def get_log_data(self) -> Dict:
    data = requests.get(self.base_url)
    #print(data.content,data.status_code)
    return data.json()

#b'Cast to ObjectId failed for value "credentials" (type string) at path "_id" for model "ResourceTree"\nCastError: Cast to ObjectId failed for value "credentials" (type string) at path "_id" for model "ResourceTree"\n    at SchemaObjectId.cast (/app/node_modules/mongoose/lib/schema/objectId.js:250:11)\n    at SchemaObjectId.SchemaType.applySetters (/app/node_modules/mongoose/lib/schemaType.js:1219:12)\n    at SchemaObjectId.SchemaType.castForQuery (/app/node_modules/mongoose/lib/schemaType.js:1633:15)\n    at cast (/app/node_modules/mongoose/lib/cast.js:375:32)\n    at model.Query.Query.cast (/app/node_modules/mongoose/lib/query.js:4768:12)\n    at model.Query.Query._castConditions (/app/node_modules/mongoose/lib/query.js:2200:10)\n    at model.Query._findOne (/app/node_modules/mongoose/lib/query.js:2484:8)\n    at model.Query.exec (/app/node_modules/mongoose/lib/query.js:4290:80)\n    at runMicrotasks (<anonymous>)\n    at processTicksAndRejections (node:internal/process/task_queues:96:5)'
