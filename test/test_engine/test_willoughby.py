import unittest
import sys
sys.path.append('C:\\Users\\nhung\\forage-lyft-starter-repo')
from engine.willoughby_engine import WilloughbyEngine

class TestSpindler(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
