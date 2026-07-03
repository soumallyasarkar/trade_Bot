
""" to check order status """
# from bot.orders import OrderManager

# order_id = int(input("Enter Order ID: "))

# response = OrderManager.get_order_status(
#     "BTCUSDT",
#     order_id,
# )

# print(response)

""" to check position"""
# from bot.orders import OrderManager

# position = OrderManager.get_position("BTCUSDT")

# print(position)



""" to check wallet balance """
# from bot.orders import OrderManager

# balances = OrderManager.get_wallet_balance()

# for asset in balances:
#     if asset["asset"] == "USDT":
#         print(asset)


""" to check open orders """
# from bot.orders import OrderManager

# orders = OrderManager.get_open_orders("BTCUSDT")

# for order in orders:
#     print(order)


""" to check cancelling an order """
# from bot.orders import OrderManager
# order_id = int(input("Enter Order ID to cancel: "))
# response = OrderManager.cancel_order(
#     "BTCUSDT",
#     order_id,
# )

# print(response)