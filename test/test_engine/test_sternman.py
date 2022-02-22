import unittest
import sys
sys.path.append('C:\\Users\\nhung\\forage-lyft-starter-repo')
from engine.sternman_engine import SternmanEngine

class TestSpindler(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())
