from audioop import cross
import json
import requests
from blockchair.exceptions import APIError, FormatError

class Blockchair:
    def __init__(self) -> None:
        self.chains = ["bitcoin", "bitcoin-cash", "litecoin", "bitcoin-sv",
                       "dogecoin", "dash", "groestlcoin", "zcash", "ecash",
                       "ethereum", "ripple", "stellar", "monero", "cardano"
                       "mixin", "tezos", "eos", "cross-chain"]
        self.cross_chain_coins = ["tether", "usd-coin", "binance-usd"]
        self.testnets = ["bitcoin", "ethereum"]

    def stats(self, chain=None, testnet=False, cross_chain_coin=None) -> json:
        payload = "https://api.blockchair.com/"
        if chain is None:
            payload += "stats"
        elif chain in self.chains:
            payload += chain
            if testnet:
                if chain in self.testnets:
                    payload += "/testnet"
                else:
                    raise FormatError(
                        chain + " does not have a supported testnet."
                    )
            elif chain == "cross-chain":
                if cross_chain_coin in self.cross_chain_coins:
                    payload += "/" + cross_chain_coin
                else:
                    raise FormatError(
                        cross_chain_coin + " is not a supported cross-chain coin."
                    )
            elif cross_chain_coin is not None:
                raise FormatError(
                    "Please specify the chain as 'cross-chain' if you'd like to explore " + cross_chain_coin
                )
            payload += "/stats"
        else:
            raise FormatError(
                "Please enter a supported chain."
            )
        
        r = requests.get(payload)
        if r.status_code != 200:
            raise APIError(
                r.reason,
                r.status_code
            )
        else:
            return r.json()

    