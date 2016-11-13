from experience import Experience
from environment import Environment
from models import Char
from observers import StateObserver
from nnGA import IndividualNNGA
from random import randint

class ExperienceCycleXY(Experience):
    def __init__(self):
        model = Char(x=300, y=300, theta=0, speed=7, dt=0.5)
        env = Environment()
        observer = StateObserver(env, model)
        controller = IndividualNNGA(observer.getDim(), 3, model.cmd_size)
        super(ExperienceCycleXY, self).__init__(model, controller, observer, timeLimit=10)

    def reset(self):
        self.model.x = randint(0, 400)
        self.model.y = randint(0, 400)
        self.model.theta = 0
        self.model.speed = 5
        self.model.X = [self.model.x, self.model.y, self.model.theta]
        self.time = 0
        self.hist = []
        self.hist.append([self.model.X, self.time])

