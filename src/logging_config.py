import logging

import logging

from config import LOG_PATH

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
    handlers=[
        logging.FileHandler(LOG_PATH+'/app.log'),
        logging.StreamHandler()
    ]
)