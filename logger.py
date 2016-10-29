#! /usr/bin/env python3
import time
import sys
__isatty__=sys.stdout.isatty()
class Logger():
    def __init__(self, level=0, colour=True):
        self.colour=bool(colour)
        if level<1:
            self.level=0
        elif level<2:
            self.level=1
        elif level<3:
            self.level=2
        else:
            self.level=0
            self.error('Specified log level(%s) not in allowed levels [0, 1, 2]' % level)
            self.info('Log level 0 assumed')
    def colourprint(self, msg, colour=1):
        self.colourprint=lambda msg, colour=1:print(msg)
        if self.colour:
            if __isatty__:
                if 'idlelib' not in list(sys.modules):
                    self.colourprint=lambda msg, colour=1:print('\033[0;%sm%s\x1b[0m' % (colour, msg))
                else:
                    self.colourprint=lambda msg, colour=1:print(msg, file=sys.stdout if colour!=31 else sys.stderr)
        self.colourprint(msg, colour=colour)
    def info(self, msg):
        if self.level==0:
            msg=[time.strftime('[%H:%M:%S]'),
                 '[INFO]',
                 str(msg)]
            self.colourprint(' '.join(msg),32)
    def warning(self, msg):
        if self.level<2:
            msg=[time.strftime('[%H:%M:%S]'),
                 '[WARNING]',
                 str(msg)]
            self.colourprint(' '.join(msg),33)
    def error(self, msg):
        msg=[time.strftime('[%H:%M:%S]'),
             '[ERROR]',
             str(msg)]
        self.colourprint(' '.join(msg),31)

if __name__=='__main__':
    logger=Logger()
    logger.colourprint('Is a tty: %s' % __isatty__)
    logger.info('this is some infomation')
    logger.warning('this is a warning')
    logger.error('this is a critical error')
    sys.stderr.write('hi')