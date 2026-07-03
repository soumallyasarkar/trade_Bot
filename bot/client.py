"""
Binance Futures Testnet client.

This module creates and returns a configured Binance client
for interacting with the Binance Futures Testnet.
"""

from binance.client import Client
from binance.exceptions import BinanceAPIException

from bot.config import API_KEY, API_SECRET, TESTNET_URL
from bot.logger import logger



class BinanceClient:
    """Wrapper class for Binance Futures Testnet."""

    def __init__(self) -> None:
        self.client = Client(API_KEY, API_SECRET)
        # Futures Testnet endpoint
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def test_connection(self) -> bool:
        """
        Test API connectivity.

        Returns:
            bool: True if connection succeeds, False otherwise.
        """
        try:
            self.client.futures_ping()
            logger.info("Connected to Binance Futures Testnet.")
            return True

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            return False

        except Exception as e:
            logger.error(f"Connection Error: {e}")
            return False

    def get_client(self) -> Client:
        """Return the configured Binance client."""
        return self.client