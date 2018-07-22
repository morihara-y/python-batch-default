import os
from ConfigParser import ConfigParser
import logging


class LoggingLib(object):
    def get_logger(self, app_home):
        logger = logging.getLogger()
        config = __get_log_conf(app_home)
        logger = __set_log_level(logger, config)
        logger = __set_file_handler(logger, app_home, config)
        return logger

    def __get_log_config(app_home):
        config = ConfigParser()
        config_path = os.path.join(app_home, "conf", "log.conf")
        config.read(config_path)
        return config

    def __set_log_level(logger, config):
        logger.setLevel(config.get("log_setting", "level"))
        return logger

    def __set_file_handler(logger, app_home, config):
        prog_name = os.path.splitext(os.path.basename(__file__))[0]
        file_handler = logging.FileHandler(os.path.join(
            app_home, "log", prog_name + ".log"), "a+")
        log_format = logging.Formatter(config.get("log_setting", "format"))
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
        return logger
