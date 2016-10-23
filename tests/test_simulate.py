# -*- coding: utf-8 -*-
"""
    Alaa El Jawad
    ~~~~~~~~~~~~~
    Module for testing how to max a function using Evolvable and HillClimber
"""
from random import random
from pybrain.structure.evolvables.evolvable import Evolvable
from pybrain.optimization import HillClimber
from models.sailboat import Sailboat
from math import pi


class SailboatEvo(Evolvable):
    def __init__(self, rudder, deltasmax):
        self.sailboat = Sailboat()
        rudder = max(-pi, min(rudder, pi))
        deltasmax = max(-pi / 2, min(deltasmax, pi / 2))
        self.cmd = [rudder, deltasmax]

    def mutate(self):
        rudder, deltasmax = self.cmd
        rudder = max(-pi, min(rudder + random() - 0.5, pi))
        deltasmax = max(-pi / 2, min(deltasmax + random() - 0.5, pi / 2))
        self.cmd = [rudder, deltasmax]

    def copy(self):
        return SailboatEvo(*self.cmd)

    def randomize(self):
        rudder = 2 * pi * random() - pi
        deltasmax = pi * random() - pi / 2
        self.cmd = [rudder, deltasmax]

    def __repr__(self):
        txt = 'Position: ({},{})\tCMD: ({},{})'
        txt = txt.format(self.sailboat.x, self.sailboat.y,
                         round(self.cmd[0], 3), round(self.cmd[1], 3))
        return str(txt)

    def fitness(self):
        for t in xrange(1, 100):
            self.sailboat.simulate(self.cmd, -1, -pi / 2)
        return (self.sailboat.x ** 2 + self.sailboat.y ** 2) ** 0.5


x0 = SailboatEvo(-2, 0.5)
le = HillClimber(lambda x: x.fitness(), x0, minimize=False, maxEvaluations=500)
le.learn()
print le.bestEvaluable, le.bestEvaluation
print x0
