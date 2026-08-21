import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

try:
    1 / 0
except ZeroDivisionError:
    logger.exception("An error occurred")

logging.basicConfig(level=logging.WARNING)
logging.info("This won't show (below WARNING)")
logging.warning("This will show")
