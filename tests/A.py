from pybrain.optimization import GA
class A(object):
    def __init__(self, x, y=10):
        self.x = x
        self.y = y


class B(A):
    def __init__(self, x):
        super(B, self).__init__(x, y=27)


if __name__ == '__main__':
    b = B(12)
    print b.x, b.y