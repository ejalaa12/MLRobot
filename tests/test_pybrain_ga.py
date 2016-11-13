import pybrain
import numpy as np
from pybrain.optimization import *
def f(x): return np.exp(-(x[0]-3)**2)

def f2(x): return -np.abs(x[0]-2) + 5 - np.abs(x[1])

init = [1, 0]
opt = GA(f2, init, minimize=False, verbose=True, storeAllEvaluated=True, maxLearningSteps=1000)
net, res  = opt.learn()
print net, res
print opt.bestEvaluable, opt.bestEvaluation

# opt = HillClimber(f, init, minimize=True, verbose=True, maxEvaluations=50, storeAllEvaluated=True)
# opt.learn()