import logging
from CompressingRotatingFileHandler import CompressingRotatingFileHandler
from LogItem import LogItem
from fastapi import FastAPI

logger = logging.getLogger('log_appender')

app = FastAPI()

@app.get("/health")
def health_check():
    return "healthy"

@app.post("/logging")
def log_appender(logItem: LogItem):
    fileHandler = None
    if(logItem.add_time_field):
        formatter = logging.Formatter("[%(asctime)s][%(levelname)s]%(message)s", "%Y-%m-%d %H:%M:%S")
    else:
        formatter = logging.Formatter("[%(levelname)s]%(message)s")
    
    fileHandler = CompressingRotatingFileHandler("../logs/log_appender.log", maxBytes=10000000, backupCount=9)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    logger.log(logItem.level.value, logItem.message)
    return {"log_devel": logItem.level, "log_message": logItem.message}