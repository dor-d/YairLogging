# module2.py
import getLogger

log = getLogger.getLogger('module2')


def foo():
    log.error('Hi from module2.py')

if __name__ == '__main__':
    foo()