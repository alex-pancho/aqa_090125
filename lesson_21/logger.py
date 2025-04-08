import logging


logging.basicConfig(
        filename='hb_test.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
