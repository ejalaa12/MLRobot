# Generator example
from pybrain.tools.shortcuts import buildNetwork
from random import randint, random
from nnGA.individual import IndividualNNGA
from nnGA.population import PopulationNNGA


def geni(s):
    for i in range(s):
        net = buildNetwork(1, 3, 1)
        yield net.params


def testIndividual():
    print "==========Testing Individual=========="
    i = IndividualNNGA(randint(1, 3), randint(3, 6), randint(1, 3))
    i.setFitness(3)
    print "params:", i.net.params
    print "fitness:", i.fitness
    print "## After Mutation"
    i.mutate()
    print "params:", i.net.params


def testPopulation():
    print "==========Testing Population=========="
    p = PopulationNNGA(4, 0.5, nn_inputs=2, nn_outputs=1)
    p.generateInitialPop()
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
