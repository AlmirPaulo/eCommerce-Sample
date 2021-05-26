import logging


#Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='server.log', format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')
