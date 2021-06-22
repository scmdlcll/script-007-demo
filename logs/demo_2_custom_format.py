import logging
import time

format = '%(relativeCreated)6d %(name)s - %(levelname)s %(message)s'
# format = 'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format)
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
logger.error('example of error message')
time.sleep(0.1)
logger.warn('example of warning message')
time.sleep(0.2)
logger.info('example of information message')
logger.debug('example of debug message')
