import os
import sys
from configparser import ConfigParser

# Set ${app_home} to application home as parent directory
app_home = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), ".."))

# set logger
logger = LoggingLib().get_logger(app_home)

# Add ${app_home}/lib as library path
sys.path.append(os.path.join(app_home, "lib"))

from logging_lib import LoggingLib
from sample_lib import SampleLib

if __name__ == "__main__":
    # set config
    config = ConfigParser()
    conf_path = os.path.join(app_home, "conf", "batch.conf")
    config.read(conf_path)

    # Sample Lib
    sampleLib = SampleLib()

    # main
    logger.info("start")
    logger.info(config.get("test", "test"))
    logger.info(sampleLib.sample())
    logger.info("end")
