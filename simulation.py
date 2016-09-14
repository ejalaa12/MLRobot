import numpy as np
import matplotlib.pyplot as plt
from DubinsCar import DubinsCar
from Environment import Environment


def gen1(d):
    return np.radians(10)


def randomDubins():
    car = DubinsCar(theta=np.radians(45), speed=10)
    x, y = np.zeros(100), np.zeros(100)
    for i in xrange(100):
        angle = np.radians(np.random.randint(0, 180))
        angle *= np.random.choice([-1, 1])
        car.sim_for_dt(angle)
        x[i] = car.x
        y[i] = car.y
    plt.plot(x, y)
    plt.axis('square')
    plt.show()


def testEnvironment():
    env = Environment()
    # env = Environment(regulator=gen1)
    env.car.speed = 20
    env.simUntilCollision()
    env.plotPath()

if __name__ == '__main__':
    # randomDubins()
    testEnvironment()
