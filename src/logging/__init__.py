import logging
import os
from logging.handlers import RotatingFileHandler

import yaml


def read_configuration(file_name):
    """
    :param file_name:
    :return: all the configuration constants
    """
    with open(file_name, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except Exception as e:
            print(f"Failed to load Configuration. Error: {e}")


config = read_configuration("src/logging/logger_conf.yml")

logging_config = config["logger"]


def get_logger():
    """
     Creates a rotating log
     """
    __logger__ = logging.getLogger('printable')
    __logger__.setLevel(logging_config["level"].upper())
    log_formatter = '%(asctime)s - %(levelname)-6s - [%(threadName)5s:%(funcName)5s():''' \
                    '%(lineno)s] - %(message)s'
    time_format = "%Y-%m-%d %H:%M:%S"
    file_path = logging_config["file_path"]
    formatter = logging.Formatter(log_formatter, time_format)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    log_file = os.path.join(file_path, f"{logging_config['name']}.log")

    temp_handler = RotatingFileHandler(log_file,
                                       maxBytes=logging_config["max_bytes"],
                                       backupCount=logging_config["back_up_count"])
    temp_handler.setFormatter(formatter)
    __logger__.addHandler(temp_handler)

    return __logger__


logger = get_logger()
