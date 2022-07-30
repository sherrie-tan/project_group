import csv
from pathlib import Path
fp = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"
#print(fp)

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    coh_list = []
    
    for line in reader:
        coh_list.append(line)
    #print(coh_list)
    
    coh_amt_list = []
    for sublist in coh_list:

        coh_amt_list.append(int(sublist[1]))
    print(coh_amt_list)

    zipped_list = zip(coh_amt_list[:-1], coh_amt_list[1:])
    diff_list = [next_element - first_element for first_element, next_element in zipped_list]
    print(diff_list)

    for sublist in diff_list:
        if sublist < 0:
            print(sublist)

fp = Path.cwd()/"project_group"/"summary_report.txt"
 
with fp.open(mode="w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["CASH DEFICT"])




      

    

    

    
    


    

        

    
  






    




