import logging
import os


LOG_CONFIG = {
    'version': 1,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'std',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        },
        'std_fh': {
            'level': 'DEBUG',
            'formatter': 'std',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(__file__), 'root.log'),
        }
    },
    'loggers': {
        'my_logger': {
            'level': 'DEBUG',
            'handlers': ['std_fh', 'console'],

        }
    },
    'formatters': {
        'std': {
            'format': '[%(asctime)s] [%(levelname)s] [%(module)s] - %(message)s'
        },

    }
}

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('my_logger')
