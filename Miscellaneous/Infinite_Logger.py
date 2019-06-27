import logging
import time
import random
import string

logging.basicConfig(filename="continuous_log.log",
                    datefmt='%H:%M:%S',
                    format='%(asctime)s.%(msecs)03d | %(name)10.10s | %(levelname).4s | %(message)s',
                    level=logging.INFO)

logger = logging.getLogger("main")


while True:
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
    logger.info("Random Log Stirng - {}".format(random_string))
    time.sleep(1)
