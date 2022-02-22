import unittest
import sys
sys.path.insert(1, 'C:\\Users\\nhung\\forage-lyft-starter-repo')
from battery.nubbin_battery import NubbinBattery
from datetime import datetime

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.datetime(2022, 1, 1)
        last_service_date = datetime.datetime(2017, 1, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.datetime(2022, 1, 1)
        last_service_date = datetime.datetime(2029, 1, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
