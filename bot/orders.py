"""
Order management for Binance Futures Testnet.
"""

from typing import Any, Dict
from binance.exceptions import BinanceAPIException
from bot.client import BinanceClient
from bot.logger import logger
import time
# Reuse a single client instance
client = BinanceClient().get_client()


class OrderManager:
    """Handles Binance Futures orders."""

    @staticmethod
    def place_market_order(
        symbol: str,
        side: str,
        quantity: float,
    ) -> Dict[str, Any]:
        """
        Place a MARKET order.
        """
        try:
            logger.info(
                f"MARKET ORDER | Symbol={symbol} Side={side} Qty={quantity}"
            )

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
            )

            order_id = response["orderId"]

            # Give Binance a moment to process
            time.sleep(0.5)

            final_response = client.futures_get_order(
                symbol=symbol,
                orderId=order_id,
            )

            logger.info(
                f"Order Filled | "
                f"OrderID={order_id} | "
                f"Status={final_response['status']}"
            )

            return final_response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise

        except Exception as e:
            logger.exception(e)
            raise

    @staticmethod
    def place_limit_order(
        symbol: str,
        side: str,
        quantity: float,
        price: float,
    ) -> Dict[str, Any]:
        """
        Place a LIMIT order.
        """
        try:
            logger.info(
                f"LIMIT ORDER | Symbol={symbol} Side={side} Qty={quantity} Price={price}"
            )

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )
            order_id = response["orderId"]
            time.sleep(0.5)
            final_response = client.futures_get_order(
                symbol=symbol,
                orderId=order_id,
            )
            return final_response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise

        except Exception as e:
            logger.exception(e)
            raise
    
    @staticmethod
    def get_order_status(
        symbol: str,
        order_id: int,
    ) -> Dict[str, Any]:
        """
        Get the latest status of an order.
        """
        return client.futures_get_order(
            symbol=symbol,
            orderId=order_id,
        )