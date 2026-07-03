"""
Input validation for the Trading Bot.
"""

from typing import Optional


SUPPORTED_ORDER_TYPES = {"MARKET", "LIMIT"}
SUPPORTED_SIDES = {"BUY", "SELL"}


def validate_symbol(symbol: str) -> str:
    """
    Validate trading symbol.

    Returns:
        Uppercase symbol.

    Raises:
        ValueError
    """
    symbol = symbol.strip().upper()

    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT Futures symbols are supported.")

    return symbol


def validate_side(side: str) -> str:
    """
    Validate BUY/SELL.
    """
    side = side.strip().upper()

    if side not in SUPPORTED_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    return side


def validate_order_type(order_type: str) -> str:
    """
    Validate MARKET/LIMIT.
    """
    order_type = order_type.strip().upper()

    if order_type not in SUPPORTED_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT.")

    return order_type


def validate_quantity(quantity: float) -> float:
    """
    Validate quantity.
    """

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return quantity


def validate_price(price: Optional[float], order_type: str) -> Optional[float]:
    """
    Validate limit price.
    """

    if order_type == "LIMIT":

        if price is None:
            raise ValueError("LIMIT orders require a price.")

        if price <= 0:
            raise ValueError("Price must be greater than zero.")

    return price