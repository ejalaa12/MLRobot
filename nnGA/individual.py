# -*- coding: utf-8 -*-
"""
    Alaa El Jawad
    ~~~~~~~~~~~~~
    Individual Neural Network for Genetic Algorithm
"""
from random import random
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer


class IndividualNNGA(object):
    """Individual network set of params"""

    def __init__(self, inputs, hidden, outputs):
        super(IndividualNNGA, self).__init__()
        self.inputs = inputs
        self.hidden = hidden
        self.outputs = outputs
        self.net = buildNetwork(inputs, hidden, outputs, outclass=TanhLayer)

    def setFitness(self, fitness):
        self.fitness = fitness

    def mutate(self):
        self.net.mutate()

    def getNetwork(self):
        return self.net

    def setNetworkParams(self, params):
        for i, v in enumerate(self.net.params):
            self.net.params[i] = params[i]

    def getcmd(self, observation):
        return self.net.activate(observation)
