# importing modules requests, json and Path 
from pathlib import Path
import requests, json

# creating a function called api_function
def api_function():
    
    # assigning api key to api_key
    api_key = "DD9WVI6K24NE4SZ7"
    # assigning link to url 
    # using f strings to insert api_key 
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'
    
    # assigning reponse to data extracted from url 
    response = requests.get(url)
    
    # .json() to retrieve data from response and save it as CURRENCY_EXCHANGE_RATE
    CURRENCY_EXCHANGE_RATE = response.json()


    # creating empty list: forex_list to store exchange rate extracted from CURRENCY_EXCHANGE_RATE
    forex_list = []
    
    # using for loop to execute data from each item 
    for value in CURRENCY_EXCHANGE_RATE:
        
        # assigning forex to exchange rate extracted from CURRENCY_EXCHANGE_RATE
        forex = CURRENCY_EXCHANGE_RATE[value]["5. Exchange Rate"]
        
        # assigning forex to from_currency symbol extracted from CURRENCY_EXCHANGE_RATE
        from_currency = CURRENCY_EXCHANGE_RATE[value]["1. From_Currency Code"]
        
        # assigning forex to to_currency symbol extracted from CURRENCY_EXCHANGE_RATE
        to_currency = CURRENCY_EXCHANGE_RATE[value]["3. To_Currency Code"]
        

    # assigning fp to file path of summary_report.txt
    fp = Path.cwd()/"project_group"/"summary_report.txt"
    
    # using .open() to open summary_report.txt
    # opening file in read mode to read the file
    with fp.open(mode="w", encoding="UTF-8",newline="") as file:
        # using .write() to write in from_currency, to_currency and forex
        file.write("[REAL TIME CURRENCY CONVERSION RATE]" " "f"{from_currency}1 = {to_currency}{forex}")





   

    


