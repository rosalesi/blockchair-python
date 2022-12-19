import unittest

from blockchair import Blockchair
from blockchair import FormatError

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

    """
    Tests for the blocks function
    """
    def testBlocks(self):
        bc = Blockchair()

        """
        Exception handling testing for the blocks() method.
        """
        with self.assertRaises(FormatError):
            result = bc.blocks("ripple", ["0"])

        with self.assertRaises(FormatError):
            result = bc.blocks("bitcoin", [])

    def testTransactions(self):
        bc = Blockchair()

        tx = bc.transactions("ethereum", ["0xf536bdfb88fa7fcc160ceeb572458eb35f7a6af3a32b7e756d6661cf08a43cf5"])

        print(len(tx.items()))
        """
        Exception handling testing for the transactions() method.
        """
        with self.assertRaises(FormatError):
            result = bc.transactions("bitcoin", [])

        with self.assertRaises(FormatError):
            result = bc.transactions("ripple", ["0"])





if __name__ == '__main__':
    unittest.main()