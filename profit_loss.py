import csv
from pathlib import Path
import re

# creating fp_read to read the csv file
fp_read = Path.cwd()/"project_group"/"csv_reports"/"Profits and Loss.csv"
# creating fp_write to write in the summary report
fp_write = Path.cwd()/"project_group"/"summary_report.txt"

# creating a function with forex as the parameter
def profitloss_function(forex):
    """
    This function will compute the difference in the net profit between each day
    """
    
    fp_read = Path.cwd()/"project_group"/"csv_reports"/"Profits and Loss.csv"
    fp_write = Path.cwd()/"project_group"/"summary_report.txt"
    
    # opening the Profit and Loss.csv file in read mode to read the data in it     
    with fp_read.open(mode="r", encoding="UTF-8", newline='') as file:
        reader = csv.reader(file)
        
        # skip reading the headers
        next(reader)
        
        # creating an empty sublist to store data from profits and loss csv file
        profit_loss_list = []

        # extracting data and storing into profit_loss_list using append.()
        for line in reader:
            profit_loss_list.append(line)
    
        # creating empty lists for day_list and net_profit_list to store the 
        # number of days and the net profit respectively 
        day_list = []
        net_profit_list = []
        
        # appending the respective values into the empty list created before using append.()
        for sublist in profit_loss_list:
            net_profit_list.append(int(sublist[4]))
            day_list.append(int(sublist[0]))

        # creating an empty sublist to store the difference in net profit
        diff_list = []

        # using range() and len() to keep track of the number of iterations to do
        for n in range(1, len(net_profit_list)):
            diff_list.append(net_profit_list[n-1] - net_profit_list[n])
        
        # create empty list profitloass_list to store api 
        profitloss_list = []
        with fp_write.open(mode="r", encoding="UTF-8") as file:
            
            # assign api to file.read(api)
            api = file.read()
            
            # append the api into empty_list
            profitloss_list.append(api)
        

        # for loop to iterate iterables in empty_list  
        # enumerate() to return sequence in empty_list 
        for info, value in enumerate(profitloss_list):
            
            # re.search to find the exchange rate in the api
            forex = re.search(pattern="SGD.+", string=value)
            forex = forex.group()
            # exchange rate at position 3:10 in forex
            forex = float(forex[3:10])
        # create empty list to store api 
        profitloss_list = []
        
        # open txt file as read mode to append api into it 
        with fp_write.open(mode="r", encoding="UTF-8") as file:
            
            # assign api to file.read(api)
            api = file.read()
            # append the api into empty_list
            profitloss_list.append(api)
        
        # for loop to iterate iterables in empty_list  
        # enumerate() to return sequence in empty_list
        for sublist, value in enumerate(profitloss_list):
            
            # re.search to find the exchange rate in the api
            forex = re.search(pattern="SGD.+", string=value)
            forex = forex.group()
            #  exchange rate at position 3:10 in forex 
            forex = float(forex[3:10])

    # using .open() to open summary_report.txt file to append profit deficit into it 
    with fp_write.open(mode="a", encoding="UTF-8",newline="")as file:

        # using zip() to iterate over iterables in day_list and diff_list in parallel 
        for item in zip(day_list, diff_list):

            # if difference in diff_list is less than zero, write it into the txt file 
            if item[1] > 0:
                file.write("\n[PROFIT DEFICIT]" " "f"DAY: {item[0]+1}" "," " "f"AMOUNT: SGD {item[1]*forex}")
