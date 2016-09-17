import random
from matplotlib import pyplot as plt
import numpy as np

plt.ion()  # interactive mode
ydata = [0] * 50

# make plot
ax1 = plt.axes()
line, = plt.plot(ydata)
plt.ylim([0, 100])  # set the y-range

while True:
    randint = int(random.random() * 100)
    ymin = float(min(ydata)) - 10
    ymax = float(max(ydata)) + 10
    plt.ylim([ymin, ymax])
    ydata.append(randint)
    del ydata[0]
    line.set_xdata(np.arange(len(ydata)))
    line.set_ydata(ydata)  # update data
    plt.draw()  # update plot
    plt.pause(.1)
