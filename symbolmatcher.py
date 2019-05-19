"""
    This module provides look up from
    well known company names or substring
    to a NSE symbol
"""

__author__      = "Chrys Kattirisetti"
__copyright__ = "Copyright 2019 International Womens Hackathon Project"
__credits__ = ["Anahita Gottipati", "Sheryl Gomes", "Chrys Kattirisetti"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Chrys Kattirisetti"
__email__ = "chryscat@gmail.com"

import csv
import logging

# csv file name with known mappings of symbol to name
filename = "EQUITY_L.csv"

# headers
fieldnames=['NAME OF COMPANY', 'SYMBOL']
companydict = {}
nameslist= []

# Initialize the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info("Loading symbolmatcher")

# reading csv file
with open(filename, 'r') as csvfile:
    logger.info("Opened file " + filename)

    # creating a csv reader object
    csvreader = csv.DictReader(open(filename), fieldnames)

    logger.info("Created csvreader for " + filename)

    # skip the header
    headers = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        symbol = row.get(fieldnames[0])
        companyname = row.get(fieldnames[1]).lower()
        nameslist.append(companyname)
        companydict[companyname] = symbol

def findSymbol(subname):
    """
    This function returns a best guess of
    symbol given a substring
    """
    # Start with starts with search
    companykey = next(word for word in nameslist if word.startswith(subname))

    # If we didn't find anything that starts with, look for any substring
    if companykey is None:
        companykey = next((s for s in nameslist if subname.lower() in s), None)

    if companykey is not None:
        logger.info("Found key " + companykey + " for symbol " + subname)
        return companydict.get(companykey)

    logger.info("No match found for symbol " +subname)
    return None
