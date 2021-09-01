import logging

class StaticVariables:

    """
    A class namespace to store respective variables with their respective values, they will be updated as the program runs.
    Only to be used at the end.
    """

    invalid_codes = list()
    invalid_artists = list()
    invalid_groups = list()
    name_too_long = dict()
    language_not_available = dict()

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

def _downloader_logging() -> logging.Logger:
    downloader_logger = logging.getLogger('nhentaiDownloader')
    downloader_file_handler = logging.FileHandler('./logs/DownloaderLogs.log')
    downloader_file_handler.setFormatter(formatter)
    downloader_logger.addHandler(downloader_file_handler)
    return downloader_logger


def _explorer_logging() -> logging.Logger:
    explorer_logger = logging.getLogger('nhentaiExplorer')
    explorer_file_handler = logging.FileHandler('./logs/ExplorerLogs.log')
    explorer_file_handler.setFormatter(formatter)
    explorer_logger.addHandler(explorer_file_handler)
    return explorer_logger


def _dbmanager_logging() -> logging.Logger:
    dbmanager_logger = logging.getLogger('nhentaiDBManager')
    dbmanager_file_handler = logging.FileHandler('./logs/DBManagerLogs.log')
    dbmanager_file_handler.setFormatter(formatter)
    dbmanager_logger.addHandler(dbmanager_file_handler)
    return dbmanager_logger


def log_and_print(level, log_type, log_msg=None, print_msg=None) -> None:
    if log_msg:
        log(level, log_msg, log_type)
    if print_msg:
        print_(print_msg)


def log(level, log_msg, log_type=''):
    if log_type == "downloader":
        logger = _downloader_logging()
    if log_type == "explorer":
        logger = _explorer_logging()
    if log_type == "dbmanager":
        logger = _dbmanager_logging()

    if level == 'info':
        logger.info(log_msg)
    if level == 'debug':
        logger.debug(log_msg)
    if level == 'warning':
        logger.warning(log_msg)
    if level == 'error':
        logger.error(log_msg)
    if level == 'critical':
        logger.critical(log_msg)

def print_(print_msg):
    print(print_msg)