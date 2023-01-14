import unittest
from datetime import datetime

from battery import NubbinBattery, SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        today = datetime.now()
        last_service1 = today.replace(year=today.year - 5)
        last_service2 = today.replace(year=today.year - 6)

        self.assertTrue(NubbinBattery(last_service1, today).needs_service())
        self.assertTrue(NubbinBattery(last_service2, today).needs_service())

    def test_doesnt_need_service(self):
        today = datetime.now()
        last_service = today.replace(year=today.year - 3)

        self.assertFalse(NubbinBattery(last_service, today).needs_service())
        self.assertFalse(NubbinBattery(today, today).needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        today = datetime.now()
        last_service1 = today.replace(year=today.year - 3)
        last_service2 = today.replace(year=today.year - 4)

        self.assertTrue(SpindlerBattery(last_service1, today).needs_service())
        self.assertTrue(SpindlerBattery(last_service2, today).needs_service())

    def test_doesnt_need_service(self):
        today = datetime.now()
        last_service = today.replace(year=today.year - 1)

        self.assertFalse(SpindlerBattery(last_service, today).needs_service())
        self.assertFalse(SpindlerBattery(today, today).needs_service())