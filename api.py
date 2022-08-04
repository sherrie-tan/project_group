from pathlib import Path
import requests, json

def api_function():
    api_key = "DD9WVI6K24NE4SZ7"
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'

    response = requests.get(url)

    CURRENCY_EXCHANGE_RATE = response.json()

    print(CURRENCY_EXCHANGE_RATE)

    for value in CURRENCY_EXCHANGE_RATE:
        forex = float(CURRENCY_EXCHANGE_RATE[value]["5. Exchange Rate"])
        from_currency = CURRENCY_EXCHANGE_RATE[value]["1. From_Currency Code"]
        to_currency = CURRENCY_EXCHANGE_RATE[value]["3. To_Currency Code"]
    
    

    


