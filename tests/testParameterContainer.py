from numpy.random import random
import numpy as np
from numpy.random.mtrand import randn
from pybrain.optimization import GA
from pybrain.structure.parametercontainer import ParameterContainer


class CmdEvolvable(ParameterContainer):
    def __init__(self, cmd):
        super(CmdEvolvable, self).__init__()
        self.cmd = cmd
        self.update_params()

    def randomize(self):
        for c in self.cmd:
            c.randomize()
        self.update_params()

    def mutate(self):
        for c in self.cmd:
            c.mutate()
        self.update_params()

    def copy(self):
        return CmdEvolvable(self.cmd)

    def __repr__(self):
        return '{}'.format(self.cmd)

    def update_params(self):
        par = []
        for x in self.cmd:
            for y in x.params:
                par += [y]
        # par = [y for y in [x.params for x in self.cmd]]
        self._setParameters(par)


class VariableEvolvable(ParameterContainer):
    def __init__(self, var, varmin, varmax):
        self.var = var
        self.varmin = varmin
        self.varmax = varmax
        super(VariableEvolvable, self).__init__()
        self._setParameters([float(self.var)])
        self.respectMargin()

    def mutate(self):
        super(VariableEvolvable, self).mutate()
        self.respectMargin()

    def respectMargin(self):
        self._params[0] = max(self.varmin, min(self._params[0], self.varmax))

    def copy(self):
        return VariableEvolvable(self._params, self.varmin, self.varmax)

    def randomize(self):
        super(VariableEvolvable, self).randomize()
        self._params[:] = self.varmin + random(self.paramdim) * self.stdParams * (self.varmax-self.varmin)
        self.respectMargin()

    def __repr__(self):
        return '{} <= {} <= {}'.format(self.varmin, self._params, self.varmax)


if __name__ == '__main__':
    print '='*20
    print 'Variable EVOLVABLE'
    x = VariableEvolvable(79, 0, 10)
    print x
    x.mutate()
    print x
    x.randomize()
    print x, x.var, x.params

    print '='*20
    print 'CMD EVOLVABLE'
    cmd = [VariableEvolvable(0, -1, 5), VariableEvolvable(0, -1, 6)]
    cmd = CmdEvolvable(cmd)
    print '>> original'
    print 'par', cmd.params
    print cmd
    print '>> mutated'
    cmd.mutate()
    print 'par', cmd.params
    print cmd
    print '>> randomized'
    cmd.randomize()
    print 'par', cmd.params
    print cmd


    # print '='*20
    # print 'GA0'
    # le = GA(lambda x: (x._params[0] / 3 - 4)**3 - 3 * x._params[0] + 20, x, minimize=False, maxEvaluations=500)
    # le.learn()
    # print le.bestEvaluable, le.bestEvaluation

    # print '=' * 20
    # print 'GA1'
    # funcm = lambda x: np.cos(x[0].params[0]) + np.sin(x[1].params[0])
    # le = GA(funcm, [VariableEvolvable(0, -1, 1), VariableEvolvable(0, 0, 1)], minimize=False, maxEvaluations=500)
    # le.learn()
    # print le.bestEvaluable, le.bestEvaluation
    print '=' * 20
    print 'GA2'
    le = GA(lambda x: -np.abs(x.params[0]-2) + 5 - np.abs(x.params[1]), cmd, minimize=False, maxEvaluations=1000)
    le.learn()
    print le.bestEvaluable, le.bestEvaluation


