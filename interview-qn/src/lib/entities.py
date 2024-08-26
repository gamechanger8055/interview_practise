import dataclasses
from enum import Enum
import pprint
from typing import Any, List

# Enums
class EntityType(Enum):
 USER = 1
 APP = 2
 
class ActivityType(Enum):
 ADD = 1
 UPDATE = 2
 DELETE = 3
 

# Dataclasses
@dataclasses.dataclass
class Attribute:
 attribute_name: str
 attribute_value: Any

 def __lt__(self, another_attribute):
    return self.attribute_name < another_attribute.attribute_name

 
@dataclasses.dataclass
class ActivityLog:
 entity_type: EntityType
 entity_id: int
 activity_type: ActivityType
 latest_attributes: List[Attribute]
 
 def __str__(self):
  return pprint.pformat(dataclasses.asdict(self))

