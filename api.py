from pathlib import Path
import requests, re

api_key = "DD9WVI6K24NE4SZ7"
url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'

r = requests.get(url)
data = r.json()
print(data)
#print(data["Realtime Currency Exchange Rate"])


#fp = Path.cwd()/"project_group"/"summary_report.txt"

#with fp.open(mode="w",encoding="UTF-8",newline="") as file:
    #file.write("[REAL TIME CURRENCY CONVERSION RATE]" f"{data}")

