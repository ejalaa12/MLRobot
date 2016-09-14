from pybrain.tools.shortcuts import buildNetwork
from regulator import Regulator
from ga import Population, Individual


class AI_regulator(Regulator):
    """A regulator that is a NN and trained by GA"""

    def __init__(self, sensors, actuators, hidden=3):
        super(AI_regulator, self).__init__()
        # System information
        self.sensors = sensors
        self.actuators = actuators
        self.hidden = hidden
        # Network params population
        self.generation = Population(12, 0.1, 0.5)
        self.generation.generateInitialPop(self.initGen)
        # Network
        self.cIndex = 0
        self.current_net = buildNetwork(
            self.sensors, self.hidden, self.actuators)
        self.updateCurrentNet()

    def initGen(self, size):
        """
        Generator that returns Neural Network params that
        have been built using PyBrain shortcut method 'buildNetwork'
        """
        for i in range(size):
            net = buildNetwork(self.sensors, self.hidden, self.actuators)
            yield list(net.params)

    def updateCurrentNet(self):
        """
        Update the current network params.
        Uses the params of the current generation element.
        """
        for i, v in enumerate(self.current_net.params):
            self.current_net.params[i] = self.generation.pop[
                self.cIndex].params[i]

    def generate_cmd(self, sensors_data):
        """
        Activates the current neural network with the given sensors_data.
        """
        return self.current_net.activate(sensors_data)[0]

    def setScore(self, score):
        """
        Set the fitness of the current generation element
        and moves to the next element of the generation (see nextNet function)
        """
        log = "Generation: {}, Element: {}, Score {}"
        print log.format(self.generation.generationNumber, self.cIndex, score)
        self.generation.pop[self.cIndex].setFitness(score)
        self.nextNet()

    def nextNet(self):
        """
        When called loop to the next individual of the generation
        OR start with the first element of the next generation
        """
        self.cIndex += 1
        if self.cIndex < len(self.generation.pop):
            self.updateCurrentNet()
        else:
            print '-' * 30
            log = "GENERATION {}, AVERAGE {}"
            print log.format(self.generation.generationNumber, self.generation.averageFitness())
            print '#' * 30
            self.generation.generateNextPop()
            self.cIndex = 0
            self.updateCurrentNet()
