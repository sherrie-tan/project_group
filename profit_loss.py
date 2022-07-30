import csv
from pathlib import Path
fp = Path.cwd()/"project_group"/"csv_reports"/"Profits and Loss.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    profit_loss_list = []
    
    for line in reader:
        profit_loss_list.append(line)
    print(profit_loss_list)
    
    profit_loss_amt_list = []
    for sublist in profit_loss_list:

        profit_loss_amt_list.append(int(sublist[1]))
    print(profit_loss_amt_list)

    zipped_list = zip(profit_loss_amt_list[:-1], profit_loss_amt_list[1:])
    diff_list = [next_element - first_element for first_element, next_element in zipped_list]
    print(diff_list)

    # not done
