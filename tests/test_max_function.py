# -*- coding: utf-8 -*-
"""
    Alaa El Jawad
    ~~~~~~~~~~~~~
    Module for testing how to max a function using Evolvable and HillClimber
"""
from random import random
from pybrain.structure.evolvables.evolvable import Evolvable
from pybrain.optimization import HillClimber


class SimpleEvo(Evolvable):
    def __init__(self, x):
        self.x = max(0, min(x, 10))

    def mutate(self):
        self.x = max(0, min(self.x + random() - 0.3, 10))

    def copy(self):
        return SimpleEvo(self.x)

    def randomize(self):
        self.x = 10 * random()

    def __repr__(self):
        return str(self.x)

    def fitness(self):
        return (self.x / 3 - 4)**3 - 3 * self.x + 20


x0 = SimpleEvo(1.2)
x = [0., 10.]
# le = HillClimber(lambda x: x.fitness(), x0, minimize=False, maxEvaluations=500)
le = HillClimber(lambda x: -abs(x[0]+2) + 5 - abs(x[1]), x, minimize=False, maxEvaluations=500)
le.learn()
print le.bestEvaluable.params, le.bestEvaluation
print x0
