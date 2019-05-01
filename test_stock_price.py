from unittest import TestCase
from nsestocks import stock_price

class TestStock_price(TestCase):
    def test_stock_price(self):
        price = stock_price('infy')
        self.assertTrue(price != None)
