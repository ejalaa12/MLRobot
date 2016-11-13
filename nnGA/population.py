# -*- coding: utf-8 -*-
"""
    Alaa El Jawad
    ~~~~~~~~~~~~~
    Neural Network Population of Individual for GA
    Contains the method for genetic algorithm
"""
from individual import IndividualNNGA
from random import choice
from pybrain.tools.shortcuts import buildNetwork


class PopulationNNGA(object):
    """Population of network params Individuals"""

    def __init__(self, popSize, eliteRate, nn_inputs, nn_outputs, nn_hidden=3, minimize=True):
        super(PopulationNNGA, self).__init__()
        # GA parameters
        self.popSize = popSize
        self.eliteRate = eliteRate
        self.generationNumber = 0
        # NN parameters
        self.inputs = nn_inputs
        self.outputs = nn_outputs
        self.hidden = nn_hidden
        # Minimize fitness
        self.minimize = minimize

    def generateInitialPop(self):
        """
        Generate the initial population of individual.
           Size=popSize
        """
        self.pop = [IndividualNNGA(self.inputs, self.hidden, self.outputs) for i in range(self.popSize)]

    def generateNextPop(self):
        """
        Generates the next generation by doing:
        1. a natural selection
        2. a cross-over of the selection
        (see functions for more information
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
        chosens = sorted(self.pop, key=lambda ind: ind.fitness,
                         reverse=not self.minimize)[:eliteSize]
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
            child_params = [choice(gene) for gene in zip(p1.net.params, p2.net.params)]
            child = IndividualNNGA(self.inputs, self.hidden, self.outputs)
            child.setNetworkParams(child_params)
            child.mutate()
            newpop.append(child)
        return newpop

    def averageFitness(self):
        """
        Calculate and returns the average fitness of the current generation.

        .. todo:: calculate only if fitness has been set
        """
        s = sum([i.fitness for i in self.pop])
        return s / self.popSize
