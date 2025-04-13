import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Create and configure logger
logger = logging.getLogger("loan_app_logger")
logger.setLevel(logging.INFO)

# Avoid adding multiple handlers during multiple imports (e.g. Streamlit reruns)
if not logger.handlers:
    file_handler = logging.FileHandler("logs/app.log")
    stream_handler = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
