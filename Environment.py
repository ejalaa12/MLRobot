import numpy as np
import matplotlib.pyplot as plt
from DubinsCar import DubinsCar
from geometry_toolkit import *
from regulator import *
from ai_regulator import AI_regulator


class Environment():
    "Environment where the Dubins car will wander"

    def __init__(self, width=300, height=300, dt=0.1, regulator=RandomReg()):
        self.width = width
        self.height = height
        self.initEnv(dt)
        # Regulation
        self.regulator = regulator

    def initEnv(self, dt):
        self.time = 0
        self.dt = dt
        self.car = DubinsCar(x=self.width / 2, y=self.height / 2, theta=0)
        self.carPathX = []
        self.carPathY = []

    def reset(self):
        self.initEnv(0.1)

    def sim1dt(self):
        """
        Simulate the car for 1 dt
        """
        # Update the new command
        self.update_cmd()

        # Call euler method to simulate the car given the cmd
        self.car.sim_for_dt(self.cmd)
        self.time += self.dt    # increment time

        # Append the new car position to the car path
        self.carPathX.append(self.car.x)
        self.carPathY.append(self.car.y)

        # Check for collision and return True if collision
        return self.checkCollision()

    def checkCollision(self):
        """
        Check if the car has hit any of the walls
        (the walls are the limit of the canvas)
        """
        if not 0 < self.car.x < self.width:
            return True
        elif not 0 < self.car.y < self.height:
            return True
        return False

    def simUntilCollision(self):
        """
        Recursively call sim1dt until there is a collision, then stops
        and set the Score (fitness) which is the duration without collision
        """
        while not self.sim1dt():
            # Stop simulation if car survived for 100 sec
            if self.time > 100:
                print 'No colission for a long time'
                break
        print 'collision after', self.time
        self.regulator.setScore(self.time)

    def plotPath(self):
        """
        Helper method to plot the path of the car using matplotlib
        """
        plt.plot(self.carPathX, self.carPathY)
        plt.axis([0, self.width, 0, self.height])
        plt.plot(self.car.x, self.car.y, 'og', markersize=10)
        plt.show()

    def update_cmd(self):
        """
        Generates the new cmd for the car by asking the given regulator
        """
        if isinstance(self.regulator, AI_regulator):
            self.cmd = self.regulator.generate_cmd(
                [self.width / 2 - self.car.x])
        else:
            self.cmd = self.regulator.generate_cmd()
        # if self.regulator is None:
        #     self.cmd = 0
        # elif self.regulator == 'random':
        #     self.cmd = np.radians(np.random.randint(0, 180))
        #     self.cmd *= np.random.choice([-1, 1])
        # else:
        #     self.cmd = self.regulator(self.front_distance())

    def find_angles(self):
        """
        __ Helper method for front distance
        .. todo: move to geometry_tookit module
        """
        x, y = self.car.x, self.car.y
        # Angle 1: corner width, height
        alpha1 = np.arctan((self.height - y) / (self.width - x))
        # Angle 2: corner 0    , height
        alpha2 = np.radians(90) + np.arctan(x / (self.height - y))
        # Angle 3: corner 0    , 0
        alpha3 = np.radians(180) + np.arctan(y / x)
        # Angle 4: corner width, 0
        alpha4 = np.radians(270) + np.arctan((self.width - x) / y)
        return [alpha1, alpha2, alpha3, alpha4]

    def front_distance(self):
        """
        Calculate the distance in front of the car to the closest wall
        """
        angle = self.find_angles()
        if not (0 < self.car.x < self.width and 0 < self.car.y < self.height):
            return 0
        a, b = find_equation(self.car.x, self.car.y, self.car.theta)
        # car cross with top side: y = height
        if angle[0] < self.car.theta <= angle[1]:
            if self.car.theta == np.radians(90):
                return dist(self.car.x, self.car.y, self.car.x, self.height)
            y = self.height
            x = (y - b) / a
            return dist(self.car.x, self.car.y, x, y)

        # car cross with left side: x = 0
        elif angle[1] < self.car.theta <= angle[2]:
            if self.car.theta == np.radians(180):
                return dist(self.car.x, self.car.y, 0, self.car.y)
            x = 0
            y = b
            return dist(self.car.x, self.car.y, x, y)

        # car cross with bottom side: y = 0
        elif angle[2] < self.car.theta <= angle[3]:
            if self.car.theta == np.radians(270):
                return dist(self.car.x, self.car.y, self.car.x, 0)
            y = 0
            x = (y - b) / a
            return dist(self.car.x, self.car.y, x, y)

        # car cross with right side: x = width
        else:
            if self.car.theta == np.radians(0):
                return dist(self.car.x, self.car.y, 0, self.car.y)
            x = self.width
            y = a * x + b
            return dist(self.car.x, self.car.y, x, y)
