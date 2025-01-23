import logging
import os
from common.config import Config

# Create logger
logger = logging.getLogger(__name__)

# Set logging level based on configuration
log_level = os.getenv('LOGGING_LEVEL', Config.LOGGING_LEVEL).upper()

logger.setLevel(log_level)

# Set up console logging
console_handler = logging.StreamHandler()
console_handler.setLevel(log_level)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


#
# Explanation:
#
# Logging setup: The logger is configured to log messages with a level of INFO and above.
# logging.getLogger(__name__): Creates a logger with the current module's name.
# FileHandler: Writes log messages to a file (app.log).
# Formatter: Defines the log message format, including timestamps, log level, and the message itself.
# This logger will be used across the application to track events, errors, and other useful information.
