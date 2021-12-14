# cli.py
import module1
import module2
import module3

from getLogger import getLogger, addFileHandlerToMain

log = getLogger('main')
addFileHandlerToMain()

if __name__ == '__main__':
    log.error('Hi from cli.py')
    module1.foo()
    module2.foo()
    module3.foo()