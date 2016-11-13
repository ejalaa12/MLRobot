from observer import Observer
from math import pi

class StateObserver(Observer):
    def getObservation(self):
        super(StateObserver, self).getObservation()
        o1 = self.model.x - self.environment.width/2
        # o1 /= self.environment.width/2
        o2 = self.model.y - self.environment.height/2
        # o2 /= self.environment.height/2
        o3 = self.model.theta
        o3 = o3 % pi - pi/2
        return [o1, o2, o3]

    def getDim(self):
        super(StateObserver, self).getDim()
        return 3

