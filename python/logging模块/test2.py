import logging

logger = logging.getLogger()
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    logger.debug('deb')