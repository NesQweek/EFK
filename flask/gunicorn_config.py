import logging
import sys

gunicorn_logger = logging.getLogger('gunicorn.error')
gunicorn_logger.addHandler(logging.StreamHandler(sys.stdout))

accesslog = '-'
errorlog = '-'
loglevel = 'info'
