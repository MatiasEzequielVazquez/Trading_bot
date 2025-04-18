from binance.client import Client

def simple_strategy(client: Client):
    try:
        # Define strategy
        print("Executing trading strategy...")

        # Check balance: USDT
        balance = client.get_asset_balance(asset='USDT')
        print(f"Available balance in USDT: {balance['free']}")

        # Purchase order simulation
        order = client.order_market_buy(
            symbol='BTCUSDT', # Trading pair
            quantity = 0.001  # Quantity to buy
        )

        print(f"Purchase order placed: {order}")
    except Exception as e:
        print(f"An error occurred in the strategy: {e}")