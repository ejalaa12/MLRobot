from numpy import array


class SimulationModel(object):
    """Abstract class for models for simulation"""

    def __init__(self, x=0, y=0):
        super(SimulationModel, self).__init__()
        self.x = 0
        self.y = 0
        self.X = array([self.x, self.y])

    def draw(self):
        " Function to draw the model at its current position"
        pass

    def simulate(self, u):
        pass

    def fdot(self, u):
        pass
