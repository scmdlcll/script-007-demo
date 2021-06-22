import logging

logging.basicConfig()
logger = logging.getLogger('myprogram')
logger.setLevel(logging.DEBUG)
logger.error('example of error message')
logger.warn('example of warning message')
logger.info('example of information message')
logger.debug('example of debug message')

# use formatting
logger.debug('get %i bytes', 5)

# and often used:
logging.info('{} + {} = {}'.format(1, 3, 4))
