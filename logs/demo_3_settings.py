import logging
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': 'myapp.log',
            'maxBytes': 1024 * 1024,
            'backupCount': 3,
            'level': 'DEBUG',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file'],
    }
})

logger = logging.getLogger('myprogram')
logger.error('example of error message')
logger.warn('example of warning message')
logger.info('example of information message')
logger.debug('example of debug message')
