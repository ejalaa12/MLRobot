# Generator example
from pybrain.tools.shortcuts import buildNetwork
from random import randint
from ga import *


def geni(s):
    for i in range(s):
        net = buildNetwork(1, 3, 1)
        yield net.params


def testIndividual():
    print "==========Testing Individual=========="
    i = Individual([random() for i in range(4)])
    i.setFitness(3)
    print "params:", i.params
    print "fitness:", i.fitness
    print "## After Mutation"
    i.mutate(0.1)
    print "params:", i.params


def testPopulation():
    print "==========Testing Population=========="
    p = Population(4, 0.1, 0.5)
    p.generateInitialPop(geni)
    print "pop:", p.pop
    for ind in p.pop:
        ind.setFitness(randint(0, 10))
    print "fitnesses:", [i.fitness for i in p.pop]

    print "---- Next generation"
    p.generateNextPop()
    print "pop:", p.pop


if __name__ == '__main__':
    testIndividual()
    testPopulation()
