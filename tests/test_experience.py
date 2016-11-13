import matplotlib.pyplot as plt
from pybrain.optimization import HillClimber, GA
from pybrain.tools.shortcuts import buildNetwork

from environment import Environment
from experiences import Experience
from fitnesses.fitness import *
from models import Char, Sailboat
from observers import StateObserver
from regulators import ConstantReg
from tests.testParameterContainer import CmdEvolvable, VariableEvolvable


def run1Experience():
    # model = Char(x=100, y=100, theta=0, speed=5)
    model = Sailboat(x=100, y=100, theta=-0.15, v=3)
    env = Environment(wind_dir=-1.5)
    observer = StateObserver(env, model)
    controller = ConstantReg([-0.037, -0.255])
    # controller = IndividualNNGA(observer.getDim(), 3, model.cmd_size)
    e = Experience(model=model, observer=observer,
                   model_controller=controller, timeLimit=100)
    # print '=' * 20
    # print 'PARAMETERS'
    # print '=' * 20
    # print 'Model \t\t: CHAR', model.x, model.y, model.theta
    # print 'Environment\t:', env.width, env.height, env.conditions
    # print 'Controller\t:', controller.inputs, controller.hidden, controller.outputs
    # print 'Params\t\t:', controller.net.params
    #
    # print '=' * 20
    # print 'EXPERIENCE'
    # print '=' * 20
    # print 'Run step'
    # print '-' * 20
    # e.runStep()
    # print model.x, model.y
    # print 'Run until'
    # print '-' * 20
    e.run()
    # print e.hist
    res = e.getResults()
    print 'Fitness', centerFitness(res, env.width / 2, env.height / 2)
    print res[0][-1], res[1][-1]
    return res


def plotResults(res, color):
    X, Y, A, T = res
    plt.plot(X, Y, color)
    plt.axis([0, 400, 0, 400])


def evaluateFitness(e, env):
    return centerFitness(e.getResults(), env.width / 2, env.height / 2)


def doExperienceWithRegulator(regulator):
    model = Char(x=100, y=100, theta=0, speed=5, dt=0.1)
    # model = Sailboat(x=100, y=100, theta=0, dt=0.1)
    env = Environment()
    observer = StateObserver(env, model)
    controller = regulator
    e = Experience(model=model, observer=observer,
                   model_controller=controller, timeLimit=20, pybrainImp=True)
    e.run()
    return e, env


def doExperienceWithConstantRegulator(pc, cmd):
    model = Char(x=120, y=20, theta=0.2, speed=5, dt=0.1)
    # model = Sailboat(x=100, y=100, theta=0, dt=0.1)
    env = Environment(wind_force=10)
    observer = StateObserver(env, model)
    if pc is not None:
        sailcmd = pc
        controller = ConstantReg(sailcmd.params)
    elif cmd is not None:
        sailcmd = cmd
        controller = ConstantReg(sailcmd)
    else:
        raise AttributeError

    e = Experience(model=model, observer=observer,
                   model_controller=controller, timeLimit=20, pybrainImp=False)
    e.run()
    return e, env


def runExpWithHillClimber():
    net = buildNetwork(3, 3, 2)
    learner = HillClimber(lambda x: evaluateFitness(
        x)[1], net, minimize=True, maxEvaluations=500, verbose=True)
    learner.learn()
    print learner.bestEvaluable
    print learner.bestEvaluation
    exp = evaluateFitness(learner.bestEvaluable)[0]
    exp.model.x = 100
    exp.model.y = 100
    exp.model.theta = 0
    exp.model.speed = 5
    exp.model.X = [exp.model.x, exp.model.y, exp.model.theta]
    exp.time = 0
    exp.hist = []
    exp.hist.append([exp.model.X, exp.time])
    exp.model_controller = learner.bestEvaluable
    exp.run()
    plotResults(exp.getResults(), 'g')
    plt.show()


def runExpWithGA():
    net = buildNetwork(3, 3, 2)
    learner = GA(lambda x: evaluateFitness(
        x)[1], net, minimize=True, maxEvaluations=1000, verbose=True)
    bestnet, bestres = learner.learn()
    print '#' * 50
    print '\tRESULTS'
    print '#' * 50
    print type(bestnet)
    print learner.bestEvaluable
    print learner.bestEvaluation
    exp = evaluateFitness(bestnet)[0]
    exp.model.x = 100
    exp.model.y = 100
    exp.model.theta = 0
    exp.model.speed = 5
    exp.model.X = [exp.model.x, exp.model.y, exp.model.theta]
    exp.time = 0
    exp.hist = []
    exp.hist.append([exp.model.X, exp.time])
    exp.model_controller = bestnet
    exp.run()
    plotResults(exp.getResults(), 'g')
    plt.show()


def doExpAndReturnFitness(pc, cmd):
    e, env = doExperienceWithConstantRegulator(pc, cmd)
    return evaluateFitness(e, env)


def test2():
    """With a constant regulator the best command we get is the one going around the center point
    If I want to limit the linear and rotation speed to a minimum the best is to create an
    Evolvable command (see doc)
    """
    deltar = VariableEvolvable(0, -3.14 / 2, 3.14 / 2)
    deltasmax = VariableEvolvable(0, -3.14 / 4, 3.14 / 4)
    sailcmd = CmdEvolvable([deltar, deltasmax])
    sailcmd.randomize()
    print sailcmd.params
    learner = GA(lambda x: doExpAndReturnFitness(pc=x, cmd=None), sailcmd,
                 minimize=True, maxLearningSteps=40, verbose=True, storeAllEvaluated=True)
    learner.learn()
    print learner._allEvaluated
    print learner.bestEvaluable, learner.bestEvaluation
    e, env = doExperienceWithConstantRegulator(pc=None, cmd=learner.bestEvaluable)
    plotResults(e.getResults(), 'g')
    plt.show()


if __name__ == '__main__':
    # for i in xrange(2):
    #     res = run1Experience()
    #     plotResults(res, 'r')
    #
    # plt.axis([0, 300, 0, 400])
    # plt.show()
    # runExpWithHillClimber()
    runExpWithGA()
    # test2()
