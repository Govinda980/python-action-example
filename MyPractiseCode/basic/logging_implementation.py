import logging

# Configure logging to write to a file with rotating logs
# logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='log_file.log', level=logging.DEBUG, format='%(asctime)s- %(levelname)s - %(message)s')

logging.info("Application started")
logging.error("An error occurred")

# 2024-11-23 23:27:13,828 - ERROR - An error occurred
