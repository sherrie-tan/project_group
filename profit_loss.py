import csv
from pathlib import Path

fp_read = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"
fp_write = Path.cwd()/"project_group"/"summary_report.txt"
    
def cash_on_hand_function(forex):
    fp_read = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"
    fp_write = Path.cwd()/"project_group"/"summary_report.txt"
    
    with fp_read.open(mode="r", encoding="UTF-8", newline='') as file:
        reader = csv.reader(file, skipinitialspace=True)
        rows = list(reader)
        next(rows)

        profit_loss_list = []

        for line in reader:
            profit_loss_list.append(line)

        day_list = []
        net_profit_list = []
        for sublist in profit_loss_list:
            net_profit_list.append(int(sublist[4]))
            day_list.append(int(sublist[0]))

        diff_list = []

        for n in range(1, len(net_profit_list)):
            diff_list.append(net_profit_list[n] - net_profit_list[n-1])
        print(diff_list)

        # not done
