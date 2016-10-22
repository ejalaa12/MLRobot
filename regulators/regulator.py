"""
Class for abstract Regulator
"""
import numpy as np


class Regulator(object):
    """docstring for Regulator"""

    def __init__(self, state=[], env=None):
        super(Regulator, self).__init__()

    def get_cmd(self):
        print 'not implemented'


class RandomReg(Regulator):
    """Random regulator that generates random commands"""

    def __init__(self):
        super(RandomReg, self).__init__(state=[], env=None)

    def get_cmd(self, inf=-1, sup=1, size=1):
        return inf + abs(sup - inf) * np.random.rand()


if __name__ == '__main__':
    r = RandomReg()
    print r.get_cmd()
