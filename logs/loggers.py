import logging
import os
from main import app_name

# logger = logging.getLogger(app_name)
# logger.setLevel(logging.DEBUG)

# formatter = logging.Formatter(
#     '[%(asctime)s] - %(module)s - %(levelname)s - %(message)s')

# log_path = os.path.join(os.path.dirname(__file__), 'root.log')
# fh = logging.FileHandler(log_path)
# fh.setLevel(logging.DEBUG)

# ch = logging.StreamHandler()
# ch.setLevel(logging.NOTSET)

# ch.setFormatter(formatter)
# fh.setFormatter(formatter)

# logger.addHandler(ch)
# logger.addHandler(fh)


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
            'format': '[%(asctime)s] - %(module)s - %(levelname)s - %(message)s'
        },

    }
}

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('my_logger')
