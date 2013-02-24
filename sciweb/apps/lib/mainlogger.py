import logging
class LoggerLog(object):
    """ basic logger class with logging module"""
    log = ''
    logger = ''

    def __init__(self, **kwargs):
        self.log = kwargs.get('log')
        if kwargs.get('loggerlog'):
            self.logger = kwargs.get('loggerlog')

            hdlr = logging.StreamHandler()   # Logs to stderr by default
            formatter = logging.Formatter('\n--\n  WEB / VIEWS %(asctime)s %(levelname)s %(message)s \n--\n')
            hdlr.setFormatter(formatter)
            self.logger.addHandler(hdlr)
            self.logger.setLevel(logging.INFO)
            self.logger.setLevel(logging.DEBUG)

    def write(self, msg):
        if self.log:
            self.logger.info(msg)
