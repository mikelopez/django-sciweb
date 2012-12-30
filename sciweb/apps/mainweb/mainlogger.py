class LoggerLog(object):
    """ basic logger class with logging module"""
    log = ''
    logger = ''

    def __init__(self, **kwargs):
        self.log = log
        if kwargs.get('log'):
            self.log = kwargs.get('log')
        if kwargs.get('loggerlog'):
            self.logger = kwargs.get('loggerlog')

    def write(self, msg):
        if self.log:
            self.logger.info(msg)



