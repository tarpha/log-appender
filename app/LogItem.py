from LogLevel import LogLevel
from pydantic import BaseModel
from typing import Union

class LogItem(BaseModel):
    level: Union[LogLevel, None] = LogLevel.ERROR
    message: str