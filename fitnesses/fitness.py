def distance(x, y, x0, y0):
    return ((x-x0)**2+(y-y0)**2)**0.5


def centerFitness(results, x0, y0):
    X, Y, S, T = results
    fit = 0
    if len(X) <= 20:
        return 10000
    for i in xrange(20):
        fit += distance(X[-i], Y[-i], x0, y0)
    return fit / 20
