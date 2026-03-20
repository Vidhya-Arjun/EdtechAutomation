from datetime import datetime
import logging
import os

def get_logger():
    os.makedirs("Logs",exist_ok=True)
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    log_file = f"Logs/execution_{timestamp}.log"

    logging.basicConfig(
        filename=log_file,
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    logger = logging.getLogger()
    logger.info("Logger initialized")

    return logger