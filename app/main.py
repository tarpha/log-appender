import logging
from CompressingRotatingFileHandler import CompressingRotatingFileHandler
from LogItem import LogItem
from fastapi import FastAPI

addTimeField = False
logger = logging.getLogger('log_appender')
formatter = logging.Formatter("[%(levelname)s]%(message)s")
fileHandler = CompressingRotatingFileHandler("../logs/log_appender.log", maxBytes=10000000, backupCount=9)
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

app = FastAPI()

@app.get("/health")
def health_check():
    return "healthy"

@app.post("/logging")
def log_appender(logItem: LogItem):
    global addTimeField
    if(addTimeField != logItem.add_time_field):
        if(logItem.add_time_field):
            formatter = logging.Formatter("[%(asctime)s][%(levelname)s]%(message)s", "%Y-%m-%d %H:%M:%S")
        else:
            formatter = logging.Formatter("[%(levelname)s]%(message)s")
        fileHandler.setFormatter(formatter)
        consoleHandler.setFormatter(formatter)
        addTimeField = logItem.add_time_field

    logger.log(logItem.level.value, logItem.message)
    return {"log_devel": logItem.level, "log_message": logItem.message}