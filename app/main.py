import logging
from CompressingRotatingFileHandler import CompressingRotatingFileHandler
from LogItem import LogItem
from fastapi import FastAPI

logger = logging.getLogger('appender_logger')
fileHandler = CompressingRotatingFileHandler("../logs/log_appender.log", maxBytes=10000000, backupCount=9)
formatter = logging.Formatter("[%(asctime)s][%(levelname)s]%(message)s", "%Y-%m-%d %H:%M:%S")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

app = FastAPI()

@app.post("/logging")
def log_appender(logItem: LogItem):
    logger.log(logItem.level.value, logItem.message)
    return {"log_devel": logItem.level, "log_message": logItem.message}