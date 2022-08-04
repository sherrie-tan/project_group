# import modules requests, json and Path 
from pathlib import Path
import requests, json

# create a function called api_function
def api_function():
    
    # assign api key to api_key
    api_key = "DD9WVI6K24NE4SZ7"
    # assign link to url 
    # f strings used to insert api_key 
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'
    
    # assign reponse to data extracted from url 
    response = requests.get(url)
    
    # .json to retrieve data from response and save it as CURRENCY_EXCHANGE_RATE
    CURRENCY_EXCHANGE_RATE = response.json()


    # create empty list: forex_list to store exchange rate extracted from CURRENCY_EXCHANGE_RATE
    forex_list = []
    
    # for loop to execute data from each item 
    for value in CURRENCY_EXCHANGE_RATE:
        
        # assign forex to exchange rate extracted from CURRENCY_EXCHANGE_RATE
        forex = CURRENCY_EXCHANGE_RATE[value]["5. Exchange Rate"]
        
        # assign forex to from_currency symbol extracted from CURRENCY_EXCHANGE_RATE
        from_currency = CURRENCY_EXCHANGE_RATE[value]["1. From_Currency Code"]
        
        # assign forex to to_currency symbol extracted from CURRENCY_EXCHANGE_RATE
        to_currency = CURRENCY_EXCHANGE_RATE[value]["3. To_Currency Code"]
        

    # assign fp to file path of summary_report.txt
    fp = Path.cwd()/"project_group"/"summary_report.txt"
    
    # .open() to open summary_report.txt as read mode as a file
    with fp.open(mode="w", encoding="UTF-8",newline="") as file:
        # .write() to write in from_currency, to_currency and forex
        file.write("[REAL TIME CURRENCY CONVERSION RATE]" " "f"{from_currency}1 = {to_currency}{forex}")





   

    


