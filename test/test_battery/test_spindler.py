import unittest
import sys
sys.path.insert(1, 'C:\\Users\\nhung\\forage-lyft-starter-repo')
from battery.spindler_battery import SpindlerBattery
from datetime import datetime

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.datetime(2024, 1, 1)
        last_service_date = datetime.datetime(2019, 1, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.datetime(2022, 1, 1)
        last_service_date = datetime.datetime(2021, 1, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
