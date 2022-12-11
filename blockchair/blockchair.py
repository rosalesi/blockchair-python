import requests
from blockchair.exceptions import APIError, FormatError

class Blockchair:
    def __init__(self) -> None:
        self.chains = ["bitcoin", "bitcoin-cash", "litecoin", "bitcoin-sv",
                       "dogecoin", "dash", "groestlcoin", "zcash", "ecash",
                       "ethereum", "ripple", "stellar", "monero", "cardano"
                       "mixin", "tezos", "eos", "cross-chain"]
        self.tokens = ["tether", "usd-coin", "binance-usd"]
        self.testnets = ["bitcoin", "ethereum"]

    def stats(self, chain=None, testnet=False, token=None) -> dict:
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
                if token in self.tokens:
                    payload += "/" + token
                else:
                    raise FormatError(
                        token + " is not a supported cross-chain coin."
                    )
            elif token is not None:
                raise FormatError(
                    "Please specify the chain as 'cross-chain' if you'd like to explore " + token
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
            return r.json()['data']

    def dashboards(self):
        pass
    