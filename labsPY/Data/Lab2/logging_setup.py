import logging
import os

def setup_logging(log_file_name):
    """Set up logging configuration for a specific lab."""
    log_folder = os.path.dirname(log_file_name)
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    
    logging.basicConfig(
        filename=log_file_name,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging initialized for the lab")
