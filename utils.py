import logging


# Sets up the logging configuration for the application.
# Args: logFilePath (str): The path to the log file where log entries will be written.
def setupLogging(logFilePath):
    logging.basicConfig(
        filename=logFilePath,
        level=logging.ERROR,
        format='%(asctime)s %(levelname)s:%(message)s'
    )


# Logs an error message to the log file.
#  message (str): The error message to be logged.

def logError(message):
    logging.error(message)
