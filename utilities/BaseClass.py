import inspect
import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:


    def get_logger(self):
        loggername=inspect.stack()[1][3]
        logger=logging.getLogger(loggername)
        formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        filehandler=logging.FileHandler("test_log.log")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger



