import requests, json

api_key = "DD9WVI6K24NE4SZ7"
url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'

response = requests.get(url)

CURRENCY_EXCHANGE_RATE = response.json()
    
print(json.dumps(CURRENCY_EXCHANGE_RATE, indent=4))

print(CURRENCY_EXCHANGE_RATE["Realtime Currency Exchange Rate"])


for eachIDD in CURRENCY_EXCHANGE_RATE["Realtime Currency Exchange Rate"]:
    print (eachIDD)

for eachIDD in CURRENCY_EXCHANGE_RATE["Exchange Rate"]:
    print(eachIDD['Exchange Rate'])
#for values in CURRENCY_EXCHANGE_RATE["Realtime Currency Exchange Rate"]:
    #print(values['5. Exchange Rate'])



#print(data["Realtime Currency Exchange Rate"])


#fp = Path.cwd()/"project_group"/"summary_report.txt"

#with fp.open(mode="w",encoding="UTF-8",newline="") as file:
    #file.write("[REAL TIME CURRENCY CONVERSION RATE]" f"{data}")

