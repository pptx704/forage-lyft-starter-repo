import unittest

from engine import CapuletEngine, WilloughbyEngine, SternmanEngine


class TestCapuletEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        self.assertTrue(CapuletEngine(55000, 23000).needs_service())
        self.assertTrue(CapuletEngine(30001, 0).needs_service())
        self.assertTrue(CapuletEngine(120000, 45000).needs_service())
    
    def test_should_not_be_serviced(self):
        self.assertFalse(CapuletEngine(30000, 0).needs_service())
        self.assertFalse(CapuletEngine(55000, 45000).needs_service())
        self.assertFalse(CapuletEngine(0, 0).needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        self.assertTrue(SternmanEngine(True).needs_service())
    
    def test_should_not_be_serviced(self):
        self.assertFalse(SternmanEngine(False).needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        self.assertTrue(WilloughbyEngine(65000, 4000).needs_service())
        self.assertTrue(WilloughbyEngine(60001, 0).needs_service())
        self.assertTrue(WilloughbyEngine(120000, 55000).needs_service())
    
    def test_should_not_be_serviced(self):
        self.assertFalse(WilloughbyEngine(60000, 0).needs_service())
        self.assertFalse(WilloughbyEngine(125000, 75000).needs_service())
        self.assertFalse(WilloughbyEngine(0, 0).needs_service())


if __name__ == '__main__':
    unittest.main()