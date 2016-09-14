"""
Class for abstract Regulator
"""
import numpy as np


class Regulator(object):
    """docstring for Regulator"""

    def __init__(self):
        super(Regulator, self).__init__()

    def generate_cmd(self):
        print 'not implemented'

    def setScore(self, score):
        print 'not implemented'


class RandomReg(Regulator):
    """Random regulator that generates random commands"""

    def __init__(self):
        super(RandomReg, self).__init__()

    def generate_cmd(self):
        cmd = np.radians(np.random.randint(0, 180))
        cmd *= np.random.choice([-1, 1])
        return cmd

    def setScore(self, score):
        print 'well, i am a random regulator'


if __name__ == '__main__':
    r = RandomReg()
    print r.generate_cmd()
