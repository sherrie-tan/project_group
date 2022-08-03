import csv, api, json, requests
from pathlib import Path

fp_read = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"
fp_write = Path.cwd()/"project_group"/"summary_report.txt"
#print(fp)

def cash_on_hand_function(forex):
    fp_read = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"
    fp_write = Path.cwd()/"project_group"/"summary_report.txt"
    
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
          
        coh_list = []
    
        for line in reader:
            coh_list.append(line)

        day_list = []
        coh_amt_list = []
        for sublist in coh_list:
            coh_amt_list.append(int(sublist[1]))
            day_list.append(int(sublist[0]))
    
        diff_list = []

        for n in range(1, len(coh_amt_list)):
            diff_list.append(coh_amt_list[n-1] - coh_amt_list[n])
        print(diff_list)
        








      

    

    

    
    


    

        

    
  






    




