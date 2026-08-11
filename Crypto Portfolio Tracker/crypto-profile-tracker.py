import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("himanshu-here-code")  

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

currency = input("Enter your currency (e.g., usd, eur, inr): ")
coins = {"bitcoin": 0.5, "ethereum": 2.0, "dogecoin": 1000}

coin_ids = ",".join(coins.keys())

payload = {
    'vs_currencies': currency,
    'ids': coin_ids,
    'x_cg_demo_api_key': API_KEY
}

response = requests.get(BASE_URL, params=payload)

if response.status_code == 200:
    data = response.json()
    wealth = 0
    print("-" * 40)
    print("LIVE COINS PRICE")
    print("-" * 40)
    for coin in coins:
        if coin in data and currency in data[coin]:
            price = data[coin][currency]
            amount = coins[coin]
            total_value = price * amount
            wealth += total_value
            print("-" * 40)
            print(coin.capitalize())
            print("-" * 40)
            print(f"Price:  {price} {currency.upper()}")
            print(f"Amount: {amount} {coin.capitalize()}")
            print(f"Value:  {total_value} {currency.upper()}")
        print("-" * 40)
        print(f"Total:  {wealth} {currency.upper()}")
        print("-" * 40)
        
else:
    print(f"Error {response.status_code}: {response.text}")