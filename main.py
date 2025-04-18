from config import get_client
from strategy import simple_strategy
import time

client = get_client()

def run_bot():
    print("Execution started...")
    while True:
        try:
            # Get account balance
            balance = client.get_asset_balance(asset='USDT')
            print(f"Balance: {balance['free']} USDT")

            # Execute strategy
            simple_strategy(client)
            time.sleep(10) # Wait 10 seconds between cicles
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "main":
    run_bot()