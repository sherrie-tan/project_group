# importing csv and Path from pathlib
import csv, re
from pathlib import Path

# assigning fp_read to Cash on Hand.csv file to read data in csv file
# assigning fp to summary_report.txt file to append cash deficit in
fp_read = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"
fp_write = Path.cwd()/"project_group"/"summary_report.txt"

# creating function cash_on_hand_function with parameter "forex"
def cash_on_hand_function(forex):
    """
    This function will compute the difference in cash on hand and highlight 
    the days where coh is not consecutively higher 
    """
    fp_read = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"
    fp_write = Path.cwd()/"project_group"/"summary_report.txt"
    
    # opening the Cash on Hand.csv as file as read mode to read the data in it 
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # assigning csv.reader to reader, to read the file 
        reader = csv.reader(file)
        
        # skip reading the headers
        next(reader)
        
        # creating empty list to store data from csv.file
        coh_list = []
        
        # using .append() to extract data and store into coh_list
        for line in reader:
            coh_list.append(line)
        
        # creating empty list day_list and coh_amt_list to store the day and coh amt respectively 
        day_list = []
        coh_amt_list = []
        
        # appending the respective values into the empty list created before using .append()
        for sublist in coh_list:
            coh_amt_list.append(int(sublist[1]))
            day_list.append(int(sublist[0]))
        
        # creating empty list to store difference calculated in coh amount 
        diff_list = []
        
        # creating empty_list to store api 
        empty_list = []
        
        # using .open() to open txt file
        # opening file in read mode to read it 
        with fp_write.open(mode="r", encoding="UTF-8") as file:
            
            # assigning api to file.read(api)
            api = file.read()
            
            # appending the api into empty_list 
            empty_list.append(api)
            
            # using for loop to iterate iterables in empty_list  
            # using enumerate() to return sequence in empty_list 
            for sublist, value in enumerate(empty_list):
                
                # using re.search to find the exchange rate in the api 
                forex = re.search(pattern="SGD.+", string=value)
                
                forex = forex.group()
                
                # exchange rate at position 3:10 in forex 
                forex = float(forex[3:10])
                
        # using range() and len() used to keep track of number of iterations to do 
            for n in range(1, len(coh_amt_list)):
            # subtract values using their index positions and appending the result of each subtraction to diff_list using .append()
                diff_list.append(coh_amt_list[n-1] - coh_amt_list[n])
                
                # multiply amt in diff_list with forex to convert USD to SGD
                coh_sgd = diff_list[-1] * forex
    
    # .open() to open summary_report.txt to append cash deficit into it 
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
            
            # zip() to iterate over iterables in day_list and diff_list in parallel 
            for item in zip(day_list, diff_list):
                
                # if difference in diff_list is more than zero, write it into the txt file 
                # item[0]: values of day_list 
                # item[1]: values of diff_list 
                if item[1] > 0:
                    file.write("\n[CASH DEFICIT]" " "f"DAY: {item[0]+1}" "," " "f"AMOUNT: SGD {item[1]*forex}")
 






      

    

    

    
    


    

        

    
  






    




