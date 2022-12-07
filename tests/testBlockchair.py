from audioop import cross
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
            result = bc.stats("cross-chain", cross_chain_coin="FEI")

        with self.assertRaises(FormatError):
            result = bc.stats("cross-chain", testnet=True, cross_chain_coin="usd-coin")

        with self.assertRaises(FormatError):
            result = bc.stats("bitcoin", cross_chain_coin="usd-coin")

        

if __name__ == '__main__':
    unittest.main()