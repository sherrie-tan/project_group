import csv
from pathlib import Path
fp = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"

#print(fp)

def cash_on_hand_function():
    with fp.open(mode="a", encoding="UTF-8", newline="") as file:
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
            diff_list.append(coh_amt_list[n] - coh_amt_list[n-1])
        print(diff_list)
    
    
        for item in zip(day_list, diff_list):
            if item[1] < 0:
                print(item)
    

    #fp = Path.cwd()/"project_group"/"summary_report.txt"
  
    #with fp.open(mode="w") as file: 
        #for item in zip(day_list, diff_list):
            #if item[1] < 0:
                #file.write("\n[CASH DEFICIT]" " "f"DAY: {item[0]+1}" "," " "f"AMOUNT: SGD{item[1]*forex}")









      

    

    

    
    


    

        

    
  






    




