import logging

class LogGen:
    @staticmethod
    def logGen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='../Logs/automation.log', mode='a')
        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
