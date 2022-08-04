from pathlib import Path
import requests, json


def api_function():
    api_key = "DD9WVI6K24NE4SZ7"
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'

    response = requests.get(url)

    CURRENCY_EXCHANGE_RATE = response.json()

#print(CURRENCY_EXCHANGE_RATE)

    forex_list = []
    for value in CURRENCY_EXCHANGE_RATE:
        forex = CURRENCY_EXCHANGE_RATE[value]["5. Exchange Rate"]
        from_currency = CURRENCY_EXCHANGE_RATE[value]["1. From_Currency Code"]
        to_currency = CURRENCY_EXCHANGE_RATE[value]["3. To_Currency Code"]
    
        forex_list.append(float(forex))

        for sublist in forex_list:
            forex_actual = sublist
        print(forex_actual)


    fp = Path.cwd()/"project_group"/"summary_report.txt"
    with fp.open(mode="w", encoding="UTF-8",newline="") as file:
        file.write("[REAL TIME CURRENCY CONVERSION RATE]" " "f"{from_currency}1 = {to_currency}{forex}")


  


   

    


