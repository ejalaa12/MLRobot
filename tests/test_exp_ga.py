from experiences import ExperienceCycleXY
from fitnesses.fitness import *
import matplotlib.pyplot as plt
from nnGA import IndividualNNGA, PopulationNNGA

def plotResults(res, color):
    X, Y, A, T = res
    plt.plot(X,Y, color)
    plt.axis([0, 400, 0, 400])


def runXYExp():
    exp = ExperienceCycleXY()
    exp.run()
    print exp.getResults()
    print centerFitness(exp.getResults(), exp.observer.environment.width/2, exp.observer.environment.height/2)
    plotResults(exp.getResults(), 'r')
    # plt.show()
    # exp2 should be the same
    exp.reset()
    exp.run()
    print exp.getResults()
    print centerFitness(exp.getResults(), exp.observer.environment.width/2, exp.observer.environment.height/2)
    plotResults(exp.getResults(), 'y')
    # plt.show()
    # exp3 should be different
    exp.reset()
    exp.model_controller = IndividualNNGA(exp.observer.getDim(), 3, exp.model.cmd_size)
    exp.run()
    print exp.getResults()
    print centerFitness(exp.getResults(), exp.observer.environment.width/2, exp.observer.environment.height/2)
    plotResults(exp.getResults(), 'b')
    plt.show()

def ga():
    exp = ExperienceCycleXY()
    pop_gen = PopulationNNGA(30, 0.35, exp.observer.getDim(), exp.model.cmd_size, minimize=True)
    pop_gen.generateInitialPop()
    pop = pop_gen.pop
    best, bestI, bestfit, worst, worstI, worstfit = run1gen(exp, pop)
    generation_summary(0, best, bestI, bestfit, exp, worst, worstI, worstfit)
    print '>> Generation average fitness', pop_gen.averageFitness()

    for i in range(1, 30):
        pop_gen.generateNextPop()
        pop =  pop_gen.pop
        best, bestI, bestfit, worst, worstI, worstfit = run1gen(exp, pop)
        # generation_summary(i, best, bestI, bestfit, exp, worst, worstI, worstfit)
        print '>> Generation {} average fitness'.format(i), pop_gen.averageFitness()
        print '#' * 40

    generation_summary(i, best, bestI, bestfit, exp, worst, worstI, worstfit)

    plt.show()


def run1gen(exp, pop):
    bestfit, best, bestI = 10000, None, -1
    worstfit, worst, worstI = 0, None, -1
    for i, ind in enumerate(pop):
        exp.model_controller = ind
        exp.run()
        fit = centerFitness(exp.getResults(), exp.observer.environment.width / 2, exp.observer.environment.height / 2)
        ind.fitness = fit
        # print 'Controller', i, 'Fitness', fit
        if fit <= bestfit:
            bestfit, best, bestI = fit, ind, i
        if fit >= worstfit:
            worstfit, worst, worstI = fit, ind, i
        exp.reset()
    return best, bestI, bestfit, worst, worstI, worstfit


def generation_summary(genN, best, bestI, bestfit, exp, worst, worstI, worstfit):
    plt.figure(genN)
    print '-' * 20
    print 'The best is', bestI, 'with a fitness of', bestfit
    exp.model_controller = best
    exp.run()
    plotResults(exp.getResults(), 'g')
    exp.reset()
    print 'The worst is', worstI, 'with a fitness of', worstfit
    exp.model_controller = worst
    exp.run()
    plotResults(exp.getResults(), 'r')


# runXYExp()
ga()