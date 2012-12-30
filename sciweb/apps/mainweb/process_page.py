from mainweb.models import Website, WebsitePage
from mainweb.utils import parse_website
from lib.mainlogger import LoggerLog

try:
    from settings import LOG_ON
except ImportError:
    LOG_ON = False

class PageProcessor(object):
    """ URL format http://sitename.com/linkname/filtername """
    linkname = None
    filtername = None
    logger = LoggerLog(log=LOG_ON, loggerlog=logging.getLogger('mainweb.process_page'))

    def __init__(self, request, linkname, filtername):
        self.linkname = linkname
        self.filtername = filtername
        self.request = request

    def process_page(self, linkname, filtername):
        """ 
        Here we will examine the URL and determine if it is a static
        URL, or if it is a WebsitePage
        """
        pass