
class LoggerLog:
    def __init__(self, msg, log=False):
        if log:
            logger.info(msg)
