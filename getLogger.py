import logging

from rich.logging import RichHandler


def initMainLogger():
    log = logging.getLogger('cli')

    console_handler = RichHandler()
    log.addHandler(console_handler)

    return log


def addFileHandlerToMain():
    log = logging.getLogger('cli')

    formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s')
    file_handler = logging.FileHandler(f'cli.log')
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)

    return log


def getLogger(name):
    log = logging.getLogger(f'cli.{name}')
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(message)s')
    file_handler = logging.FileHandler(f'{name}.log')
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)


    return log

initMainLogger()