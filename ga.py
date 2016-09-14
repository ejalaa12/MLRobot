"""
Classes that will make a Neural Network weights' params
evolve with a genetic algorithm.
"""
from random import choice, random


class Individual(object):
    """Individual network set of params"""

    def __init__(self, params):
        super(Individual, self).__init__()
        self.params = params

    def setFitness(self, fitness):
        self.fitness = fitness

    def mutate(self, mutationRate):
        for i, p in enumerate(self.params):
            if random() < mutationRate:
                self.params[i] = max(0, min(p + random() - 0.3, 10))


class Population(object):
    """Population of network params Individuals"""

    def __init__(self, popSize, mutationRate, eliteRate):
        super(Population, self).__init__()
        self.popSize = popSize
        self.mutationRate = mutationRate
        self.eliteRate = eliteRate
        self.generationNumber = 0

    def generateInitialPop(self, generator):
        """
        Generate the initial population of individual.
           Size=popSize
        """
        self.pop = [Individual(params) for params in generator(self.popSize)]

    def generateNextPop(self):
        """
        Generates the next generation by doing:
        1. a natural selection
        2. a cross-over of the selection
        (see functions for more informations)
        """
        self.generationNumber += 1
        elite = self.gaSelection()
        self.pop = self.crossOver(elite)

    def gaSelection(self):
        """
        Select the best elements in the current generation based on fitness
        (best elements = *eliteSize* firsts elements)
        """
        eliteSize = int(round(self.popSize * self.eliteRate))
        chosens = sorted(self.pop, key=lambda ind: ind.fitness, reverse=True)[:eliteSize]
        return chosens

    def crossOver(self, elite):
        """
        Generates a new population from the elite of the previous one.

        - Chooses two 'parents' from the elite,
        - Do a cross-over of the parents' network parameters.
        - Mutate an Individual

        :param elite: elite list from the previous generation
        """
        newpop = []
        for c in xrange(self.popSize):
            p1, p2 = choice(elite), choice(elite)   # parents
            child_params = [choice(gene) for gene in zip(p1.params, p2.params)]
            child = Individual(child_params)
            child.mutate(self.mutationRate)
            newpop.append(child)
        return newpop

    def averageFitness(self):
        """
        Calculate and returns the average fitness of the current generation.

        .. todo:: calculate only if fitness has been set
        """
        s = sum([i.fitness for i in self.pop])
        return s / self.popSize
