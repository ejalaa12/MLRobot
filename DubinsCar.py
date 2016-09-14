import numpy as np


class DubinsCar():
    " Simulation of a Dubins Car"
    def __init__(self, x=0, y=0, theta=0, speed=1):
        self.x = x
        self.y = y
        self.theta = theta
        self.speed = speed

    def fdot(self, u):
        xdot = self.speed * np.cos(self.theta)
        ydot = self. speed * np.sin(self.theta)
        thetadot = u
        return np.array([xdot, ydot, thetadot])

    def sim_for_dt(self, u, dt=0.1):
        """
        Calculate the next position using euler simulation
        with the given command
        """
        Xdot = self.fdot(u)
        self.x = self.x + Xdot[0] * dt
        self.y = self.y + Xdot[1] * dt
        self.theta = self.theta + Xdot[2] * dt
