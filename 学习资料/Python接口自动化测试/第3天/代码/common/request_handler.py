import requests
from config.settings import TIMEOUT
from common.logger import logger

def send_request(method, url, **kwargs):
    kwargs.setdefault("timeout", TIMEOUT)
    
    logger.info("request start | method=%s url=%s", method, url)
    logger.info("request kwargs | %s", kwargs)

    resp = requests.request(method=method, url=url, **kwargs)
    
    logger.info("response status | %s", resp.status_code)
    logger.info("response text | %s", resp.text)

    return resp