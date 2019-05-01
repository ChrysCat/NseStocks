from nsetools import Nse
"""This module supports two methods:
   getting stock price of a given stock.
   Alert when stock price reaches some threshold - TBD"""


def stock_price(symbol):
    """This function returns the last
	price of the given symbol"""
    nse = Nse()
    if nse.is_valid_code(symbol):
        q = nse.get_quote(symbol)
        return q.get('lastPrice', None)
    else:
        raise Exception("Unknown stock " + symbol)
