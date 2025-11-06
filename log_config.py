import logging
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("bot_log.log", encoding="utf-8")
file_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(levelname)s - %(module)s - %(message)s"
))

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(levelname)s - %(module)s - %(message)s"
))

logger.addHandler(file_handler)
logger.addHandler(console_handler)