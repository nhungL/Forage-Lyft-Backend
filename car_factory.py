import engine.capulet_engine as capulet
import engine.sternman_engine as sternman
import engine.willoughby_engine as willoughby
import battery.spindler_battery as spindler
import battery.nubbin_battery as nubbin
from car import Car
from datetime import date

class CarFactory():
    @staticmethod
    def  create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        battery = spindler.SpindlerBattery(current_date, last_service_date)
        engine = capulet.CapuletEngine(current_mileage, last_service_mileage)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        battery = spindler.SpindlerBattery(current_date, last_service_date)
        engine = willoughby.WilloughbyEngine(current_mileage, last_service_mileage)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(current_date : date, last_service_date : date, warning_light_is_on : bool) -> Car:
        battery = spindler.SpindlerBattery(current_date, last_service_date)
        engine = sternman.SternmanEngine(warning_light_is_on)
        car = Car(engine, battery)
        return car
    
    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        battery = nubbin.NubbinBattery(current_date, last_service_date)
        engine = willoughby.WilloughbyEngine(current_mileage, last_service_mileage)
        car = Car(engine, battery)
        return car
    
    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        battery = nubbin.NubbinBattery(current_date, last_service_date)
        engine = capulet.CapuletEngine(current_mileage, last_service_mileage)
        car = Car(engine, battery)
        return car