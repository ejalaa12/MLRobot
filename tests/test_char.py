from models import Char
import matplotlib.pyplot as plt

if __name__ == '__main__':
    c = Char()
    x, y = [], []
    for t in range(200):
        c.simulate([t/10-10, 1])
        x.append(c.x)
        y.append(c.y)

    plt.figure()
    plt.plot(x, y)
    plt.show()
    print c.x, c.y, c.theta