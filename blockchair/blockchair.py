import requests
from blockchair.exceptions import APIError, FormatError

class Blockchair:

    """
    Initializes Blockchair Object with it's supported chains, testnets, and tokens as 
    member variables.

    Parameters:
        None

    Returns:
        Blockchair Object
    """
    def __init__(self) -> None:
        self.btc_chains = ["bitcoin", "bitcoin-cash", "litecoin", "bitcoin-sv",
                                "dogecoin", "dash", "groestlcoin", "zcash", "ecash"]
        self.chains = self.btc_chains + ["ethereum", "ripple", "stellar", "monero", "cardano"
                                    "mixin", "tezos", "eos", "cross-chain"]
        self.tokens = ["tether", "usd-coin", "binance-usd"]
        self.testnets = ["bitcoin", "ethereum"]

    def stats(self, chain=None, testnet=False, token=None) -> dict:
        """
        Accesses Blockchair's stats endpoint for supported chains and testnets.

        Parameters:
            chain (str) : Optional. Blockchair supported chain.
            testnet (bool) : Optional. For BTC or ETH testnets.
            token (str) : Optional. For cross-chain token stats.

        Returns:
            dict 
        """

        payload = "https://api.blockchair.com/"

        if(chain and chain not in self.chains):
            raise FormatError(
                "Please enter a supported chain."
            )
        if(testnet and chain not in self.testnets):
            raise FormatError(
                chain + " does not have a supported testnet."
            )
        if(token and token not in self.tokens):
            raise FormatError(
                token + " is not a supported cross-chain coin."
            )
        if(chain and chain != "cross-chain" and token):
            raise FormatError(
                "Please specify the chain as 'cross-chain' if you'd like to explore " + token
            )

        if not chain:
            payload += "stats"
        else:
            payload += chain
            if testnet:
                payload += "/testnet"
            elif chain == "cross-chain":
                payload += "/" + token
            payload += "/stats"
        
        r = requests.get(payload)
        if r.status_code != 200:
            raise APIError(
                r.reason,
                r.status_code
            )
        return r.json()['data']

    def blocks(self, chain : str, blockNo : list) -> dict:
        """
        Interface for Blockchair's blockchain block data. Support for 
        BTC-related chains and ETH.

        Parameters:
            chain (str) : Blockchair API dashboard endpoint supported chain.
            blockNo (list[str]) : List of either block numbers of block hashes as strings
        Returns:
            dict
        """

        payload = "https://api.blockchair.com/"
        
        if(chain not in self.btc_chains
            and chain != "ethereum"):
            raise FormatError(
                "Please enter a BTC or ETH related chain."
            )
        if (len(blockNo) < 1):
            raise FormatError(
                "Please enter at least one block height or block hash."
            )

        payload += chain + "/dashboards/blocks/"
        for b in blockNo:
            payload += b + ","
        payload = payload[ : -1]
        
        r = requests.get(payload)
        if r.status_code != 200:
            raise APIError(
                r.reason,
                r.status_code
            )
        return r.json()['data']

    def transactions(self, chain : str, hashes : list):
        """
        Interface for Blockchair transaction data. Supports BTC related chains and ETH.

        Parameters:
            chain (str) : Blockchair supported BTC chains or ETH 
            hashes (list[str]) : List of transaction hashes as strings
        Returns:
            dict
        """
        
        payload = "https://api.blockchair.com/"

        if(chain not in self.btc_chains
            and chain != "ethereum"):
            raise FormatError(
                "Please enter a BTC or ETH related chain."
            )
        if (len(hashes) < 1):
            raise FormatError(
                "Please enter at least one block height or block hash."
            )

        payload += chain + "/dashboards/transactions/"
        for hash in hashes:
            payload += hash + ","
        payload = payload[ : -1]

        r = requests.get(payload)
        if r.status_code != 200:
            raise APIError(
                r.reason,
                r.status_code
            )
        return r.json()['data']

    