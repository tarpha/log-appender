from LogLevel import LogLevel
from pydantic import BaseModel
from typing import Union

class LogItem(BaseModel):
    level: Union[LogLevel, None] = LogLevel.ERROR
    namespace: Union[str, None] = 'default'
    message: str
    add_time_field: Union[bool, None] = True
