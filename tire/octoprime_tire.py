from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        return sum (self.sensors) >= 3
    


