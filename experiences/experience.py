# -*- coding: utf-8 -*-
"""
    Alaa El Jawad
    ~~~~~~~~~~~~~
    Define an experience
"""


class Experience(object):
    """An experience consist of an environment and a way to
    calculate the fitness of an individual
    """

    def __init__(self, model, model_controller, observer, timeLimit, pybrainImp=False):
        super(Experience, self).__init__()
        self.model = model
        self.model_controller = model_controller
        self.observer = observer
        # Experience duration
        self.time = 0
        self.timeLimit = timeLimit
        # Experience history
        self.hist = []
        self.hist.append([self.model.X, self.time])

        self.pybrainImp = pybrainImp

    def experienceHasEnded(self):
        collision = self.observer.checkCollision()
        endtime = self.time > self.timeLimit
        if collision:
            # print 'Collision detected... stopping experience'
            return True
        if endtime:
            # print 'Time elapsed, end of experience'
            return True
        return False

    def runStep(self):
        # print '-', self.time, '-'
        obs = self.observer.getObservation()
        if self.pybrainImp:
            u = self.model_controller.activate(obs)
        else:
            u = self.model_controller.getcmd(obs)
        # print 'obs\t', obs
        # print 'u\t', u
        self.model.simulate(u, self.observer.environment.conditions)

    def run(self):
        while not self.experienceHasEnded():
            self.runStep()
            self.time += self.model.dt
            self.hist.append([self.model.X, self.time])

    def getResults(self):
        X, Y, A, T = [], [], [], []
        for h in self.hist:
            X.append(h[0][0])
            Y.append(h[0][1])
            A.append(h[0][2])
            T.append(h[1])
        return X, Y, A, T


