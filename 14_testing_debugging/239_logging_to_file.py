import logging
import tempfile
import os

log_file = os.path.join(tempfile.gettempdir(), "app.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("myapp")

logger.info("Application started")
logger.debug("Loading configuration")
logger.warning("Config file not found, using defaults")
logger.info("Server running on port 8080")

try:
    result = 10 / 0
except ZeroDivisionError:
    logger.error("Division error occurred", exc_info=True)

with open(log_file) as f:
    print("\nLog file contents:")
    print(f.read())

os.remove(log_file)
