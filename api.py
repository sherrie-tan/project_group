import requests
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=DD9WVI6K24NE4SZ7'
r = requests.get(url)
data = r.json()
