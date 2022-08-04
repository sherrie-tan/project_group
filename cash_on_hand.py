# import csv and Path from pathlib
import csv, re
from pathlib import Path

# assign fp_read to Cash on Hand.csv file to read data in csv file
# assign fp to summary_report.txt file to append cash deficit in
fp_read = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"
fp_write = Path.cwd()/"project_group"/"summary_report.txt"

# def cash_on_hand_function with parameter "forex"
def cash_on_hand_function(forex):
    """
    This function will compute the difference in cash on hand and highlight 
    the days where coh is not consecutively higher 
    """
    fp_read = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"
    fp_write = Path.cwd()/"project_group"/"summary_report.txt"
    
    # open the Cash on Hand.csv as file as read mode to read the data in it 
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # assign csv.reader to reader, to read the file 
        reader = csv.reader(file)
        
        # skip reading the headers
        next(reader)
        
        # create empty list to store data from csv.file
        coh_list = []
        
        # .append() used to extract data and store into coh_list
        for line in reader:
            coh_list.append(line)
        
        # create empty list day_list and coh_amt_list to store the day and coh amt respectively 
        day_list = []
        coh_amt_list = []
        
        # .append() the respective values into the empty list created before
        for sublist in coh_list:
            coh_amt_list.append(int(sublist[1]))
            day_list.append(int(sublist[0]))
        

        # create empty list to store difference calculated in coh amount 
        diff_list = []
        
        api_list = []
        with fp_write.open(mode="r", encoding="UTF-8") as file:
            api_get = file.read()
            api_list.append(api_get)

            for info, value in enumerate(api_list):
                forex = re.search(pattern="SGD.+\d", string=value)
                forex = forex.group()
                forex = float(forex[3:10])
                
        # range() and len() used to keep track of number of iterations to do 
            for n in range(1, len(coh_amt_list)):
            # subtract values using their index positions and appending the result of each subtraction to diff_list using .append()
                diff_list.append(coh_amt_list[n-1] - coh_amt_list[n])
                coh_sgd = diff_list[-1] * forex
    
    # .open() to open summary_report.txt to append cash deficit into it 
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
            
            # zip() to iterate over iterables in day_list and diff_list in parallel 
            for item in zip(day_list, diff_list):
                
                # if difference in diff_list is more than zero, write it into the txt file 
                # item[0]: values of day_list 
                # item[1]: values of diff_list 
                if item[1] > 0:
                    file.write("\n[CASH DEFICIT]" " "f"DAY: {item[0]+1}" "," " "f"AMOUNT: SGD {coh_sgd}")
 

print(cash_on_hand_function)




      

    

    

    
    


    

        

    
  






    




