# used for mainweb.views controller for common functions

def parse_website(request, logger=False):
  """ return website object by http data - no mistakes"""
  sitename = request.get('HTTP_HOST')
  # remove any dev port numbers http://127.0.0.1:8888
  domain_string = sitename.split(':')[0]
  if logger:
    logger(domain_string)
  return domain_string