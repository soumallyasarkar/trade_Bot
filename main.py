from colorama import Fore, Style, init

from bot.cli import parse_arguments
from bot.orders import OrderManager
from bot.validators import (
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
    validate_symbol,
)

init(autoreset=True)


def main():
    try:
        args = parse_arguments()

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print(Fore.CYAN + "=" * 50)
        print(Fore.CYAN + " Binance Futures Testnet Trading Bot")
        print(Fore.CYAN + "=" * 50)

        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")

        if order_type == "LIMIT":
            print(f"Price       : {price}")

        print("-" * 50)

        if order_type == "MARKET":
            response = OrderManager.place_market_order(
                symbol,
                side,
                quantity,
            )
        else:
            response = OrderManager.place_limit_order(
                symbol,
                side,
                quantity,
                price,
            )

        print(Fore.GREEN + "Order placed successfully!\n")

        print(f"Order ID       : {response['orderId']}")
        print(f"Status         : {response['status']}")
        print(f"Executed Qty   : {response['executedQty']}")
        print(f"Original Qty   : {response['origQty']}")
        print(f"Average Price  : {response.get('avgPrice', 'N/A')}")
        print(f"Update Time    : {response['updateTime']}")

    except Exception as e:
        print(Fore.RED + f"Error: {e}")


if __name__ == "__main__":
    main()