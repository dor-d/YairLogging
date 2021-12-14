# module1.py
import getLogger

log = getLogger.getLogger('module1')


def foo():
    log.error('Hi from module1.py')

if __name__ == '__main__':
    foo()