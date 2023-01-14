import unittest

from tire import CarriganTire, OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_should_be_serviced(self):
        self.assertTrue(OctoprimeTire([0.9, 0.8, 0.8, 0.7]).needs_service())
        self.assertTrue(OctoprimeTire([0.9, 0, 0.9, 0.1]).needs_service())
        self.assertTrue(OctoprimeTire([1, 0, 0, 0.6]).needs_service())

    def test_should_not_be_serviced(self):
        self.assertFalse(OctoprimeTire([0, 0, 0, 0]).needs_service())
        self.assertFalse(OctoprimeTire([0.8, 0.8, 0.8, 0.8]).needs_service())

class TestCarriganTire(unittest.TestCase):
    def test_should_be_serviced(self):
        self.assertTrue(CarriganTire([0.5, 0.5, 1, 1]).needs_service())
        self.assertTrue(CarriganTire([0, 1, 1, 1]).needs_service())
        self.assertTrue(CarriganTire([0.7, 0.8, 0.7, 0.8]).needs_service())

    def test_should_not_be_serviced(self):
        self.assertFalse(CarriganTire([0.5, 0.5, 0.5, 0.5]).needs_service())
        self.assertFalse(CarriganTire([0.8, 0.8, 0.8, 0.5]).needs_service())