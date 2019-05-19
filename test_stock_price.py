from unittest import TestCase
from nsestocks import stock_price

class TestStock_price(TestCase):
    def test_stock_price(self):
        # Test with exact symbol match
        price = stock_price('infy')
        self.assertTrue(price != None)

    def test_stock_price(self):
        # Test with partial match
        price = stock_price('infosys')
        self.assertTrue(price != None)

    def test_stock_price(self):
        # Test with partial match
        price = stock_price('abb')
        self.assertTrue(price != None)