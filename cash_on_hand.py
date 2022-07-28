import csv
from pathlib import Path
fp = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"
print(fp)

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    cash_on_hand_list = []
    
    for line in reader:
        cash_on_hand_list.append(line)
    print (cash_on_hand_list)

    for sublist in cash_on_hand_list:
        print (sublist)

    

    
    


    

        

    
  






    




