"""
Class for abstract Regulator
"""
import numpy as np
import abc

class Regulator(object):
    """docstring for Regulator"""

    def __init__(self, state=[], env=None):
        super(Regulator, self).__init__()

    @abc.abstractmethod
    def getcmd(self, **kwargs):
        print 'not implemented'


class RandomReg(Regulator):
    """Random regulator that generates random commands"""

    def __init__(self):
        super(RandomReg, self).__init__(state=[], env=None)

    def getcmd(self, inf=-1, sup=1, size=1, **kwargs):
        return inf + abs(sup - inf) * np.random.rand()


class ConstantReg(Regulator):
    """Regulator that sends a constant command"""

    def __init__(self, cmd):
        super(ConstantReg, self).__init__()
        self.cmd = cmd

    def getcmd(self, *args):
        return self.cmd


if __name__ == '__main__':
    r = RandomReg()
    print r.getcmd()
