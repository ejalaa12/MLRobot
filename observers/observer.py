import abc


class Observer(object):
    def __init__(self, environment, model):
        self.environment = environment
        self.model = model

    @abc.abstractmethod
    def getObservation(self):
        "defines what to observe and returns the observation"

    def checkCollision(self):
        """
        Checks if a model that is at the position (x,y)
        has collided with the walls
        """
        if not 0 <= self.model.x <= self.environment.width:
            print 'not in (x)', self.model.x, self.environment.width
            return True
        elif not 0 <= self.model.y <= self.environment.height:
            print 'not in (y)', self.model.y, self.environment.height
            return True
        return False

    @abc.abstractmethod
    def getDim(self):
        ":return dimension of the observation"
