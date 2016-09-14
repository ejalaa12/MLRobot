from Tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from Environment import Environment
import numpy as np
from ai_regulator import AI_regulator


class Application(Frame):
    " Application window for the simulation of a simple Dubins car "

    def __init__(self, master=None, width=300, height=300, mode='square', speed=1):
        Frame.__init__(self, master)
        self.width = width
        self.height = height
        self.mode = mode
        self.speed = speed
        self.dt = 100 / speed
        self.pack()
        self.generateFrames()
        self.createWidgets()
        self.setupEnv()

    def generateFrames(self):
        self.canvas_frame = Frame(self, borderwidth=2)
        self.canvas_frame.grid(column=1, row=1, rowspan=2)

        self.button_frame = Frame(self, borderwidth=2)
        self.button_frame.grid(column=2, row=1)

        self.info_frame = Frame(self, borderwidth=2)
        self.info_frame.grid(column=2, row=2)

    def createWidgets(self):
        self.canvas = Canvas(self.canvas_frame, width=self.width,
                             height=self.height, bg='grey')
        self.canvas.grid(column=1, row=1)

        self.button_start = Button(
            self.button_frame, text='Start', command=self.start_sim)
        self.button_start.grid(column=1, row=1)

        self.button_stop = Button(
            self.button_frame, text='Stop', command=self.stop_sim)
        self.button_stop.grid(column=2, row=1)

        self.button_reset = Button(
            self.button_frame, text='Reset', command=self.reset)
        self.button_reset.grid(column=1, row=2)

        self.button_1gen = Button(
            self.button_frame, text='1gen', command=self.do1GenSim)
        self.button_1gen.grid(column=2, row=2)

    def setupEnv(self, reset=False):
        if not reset:
            reg = AI_regulator(sensors=1, actuators=1, hidden=3)
            self.env = Environment(
                width=self.width, height=self.height, regulator=reg,
                dt=0.1 / self.speed)
        else:
            self.env.reset()
        if self.mode == 'square':
            pass    # set car in the center (default mode)
        elif self.mode == 'line':
            self.env.car.x = self.width / 2
            self.env.car.y = 20
            self.env.car.theta = np.radians(90)
        self.env.car.speed = 50
        self.flag = False
        self.draw_tank(self.env.car.x, self.env.car.y, self.env.car.theta)

    def start_sim(self):
        self.flag = True
        # print '---started'
        self.do_sim()

    def do_sim(self, loop=False):
        if self.flag and not self.env.sim1dt():
            # print 'hello'
            self.canvas.delete('all')
            self.draw_tank(self.env.car.x, self.env.car.y, self.env.car.theta)
            self.drawLine(self.env.carPathX, self.env.carPathY)
            self.after(self.dt, self.do_sim, loop)
        if self.env.checkCollision() or self.env.time > 10:
            self.flag = False
            # print 'collision detected after', self.env.time, 's'
            # print 'stopped----', loop
            self.env.regulator.setScore(self.env.car.y)
            if loop:
                self.reset()
                self.after(self.dt, self.do1GenSim)

    def do1GenSim(self):
        # print 'stop > reset > start in for loop'
        if self.env.regulator.cIndex < self.env.regulator.generation.popSize:
            self.flag = True
            self.do_sim(loop=True)
        # for x in xrange(0, 12):
        #     self.start_sim()
        #     while self.flag:
        #         pass

    def stop_sim(self):
        self.flag = False
        # print 'stopped----'
        self.env.regulator.setScore(self.env.car.y)

    def reset(self):
        # print 'reseting'
        self.canvas.delete('all')
        self.setupEnv(reset=True)

    def drawLine(self, x, y):
        points = zip(x, y)
        for i in xrange(1, len(points)):
            xa, ya = points[i - 1][0], points[i - 1][1]
            xb, yb = points[i][0], points[i][1]
            self.canvas.create_line(xa, ya, xb, yb)

    def draw_tank(self, x, y, theta):
        M = np.array([[1, -1, 0, 0, -1, -1, 0, 0, -1, 1, 0, 0, 3, 3, 0],
                      [-2, -2, -2, -1, -1, 1, 1, 2, 2, 2, 2, 1, 0.5, -0.5, -1]])
        M = 5 * M  # resize Tank
        M = np.vstack((M, np.ones(M.shape[1])))
        R = np.array([[np.cos(theta), -np.sin(theta), x],
                      [np.sin(theta), np.cos(theta), y],
                      [0, 0, 1]])

        M = np.dot(R, M)
        self.drawLine(M[0], M[1])


if __name__ == '__main__':
    print '\n' * 10
    root = Tk()
    fen = Application(master=root, width=100, height=600, mode='line', speed=3)
    fen.mainloop()
    root.mainloop()
