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

x0 = SimpleEvo(1.2)
x1 = SimpleEvo(2.4)
l = HillClimber(lambda x: abs(x.x), x1, minimize=True, maxEvaluations=100)
l.learn()
print x0, x1
