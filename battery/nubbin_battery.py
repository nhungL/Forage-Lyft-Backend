from car import Car
import Battery
from datetime import date
import dateutil.relativedelta

class NubbinBattery(Car, Battery):
    def __init__(self, current_date: date, last_service_date: date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        self.current_date = date.today()
        return dateutil.relativedelta(self.last_service_date, self.current_date).years > 4

