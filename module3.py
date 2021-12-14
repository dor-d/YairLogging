# module3.py

import getLogger

log = getLogger.getLogger('module3')


def foo():
    log.error('Hi from module3.py')

if __name__ == '__main__':
    foo()