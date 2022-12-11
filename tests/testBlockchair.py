from audioop import cross
from lib2to3.pgen2 import token
import unittest

from blockchair import Blockchair
from blockchair import FormatError
from blockchair import APIError

"""
Tests for the Blockchair class
"""
class TestBlockchair(unittest.TestCase):

    """
    Test for the stats function
    """
    def testStats(self):
        bc = Blockchair()

        '''
        Exception handling testing for the stats method. Needs more coverage for proper use testing.
        '''

        with self.assertRaises(FormatError):
            result = bc.stats("solana")

        with self.assertRaises(FormatError):
            result = bc.stats("tezos", testnet=True)

        with self.assertRaises(FormatError):
            result = bc.stats("cross-chain", token="FEI")

        with self.assertRaises(FormatError):
            result = bc.stats("cross-chain", testnet=True, token="usd-coin")

        with self.assertRaises(FormatError):
            result = bc.stats("bitcoin", token="usd-coin")

if __name__ == '__main__':
    unittest.main()