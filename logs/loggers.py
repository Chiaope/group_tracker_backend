import logging
import os
from main import app_name

logger = logging.getLogger(app_name)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s] - %(module)s - %(levelname)s - %(message)s')

log_path = os.path.join(os.path.dirname(__file__), 'root.log')
fh = logging.FileHandler(log_path)
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.NOTSET)

ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)
