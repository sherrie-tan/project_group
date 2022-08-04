import csv
from pathlib import Path

fp_read = Path.cwd()/"project_group"/"csv_reports"/"Profits and Loss.csv"
fp_write = Path.cwd()/"project_group"/"summary_report.txt"
    
def profitloss_function(forex):
    fp_read = Path.cwd()/"project_group"/"csv_reports"/"Profits and Loss.csv"
    fp_write = Path.cwd()/"project_group"/"summary_report.txt"
    
    with fp_read.open(mode="r", encoding="UTF-8", newline='') as file:
        reader = csv.reader(file)

        next(reader)

        profit_loss_list = []

        for line in reader:
            profit_loss_list.append(line)
        #print(profit_loss_list)
    
        day_list = []
        net_profit_list = []
    
        for sublist in profit_loss_list:
            net_profit_list.append(int(sublist[4]))
            day_list.append(int(sublist[0]))

        diff_list = []

        for n in range(1, len(net_profit_list)):
            diff_list.append(net_profit_list[n] - net_profit_list[n-1])
        print(diff_list)

    with fp_write.open(mode="a", encoding="UTF-8",newline="")as file:
        for item in zip(day_list, diff_list):
            if item[1] < 0:
                file.write("\n[PROFIT DEFICIT" " "f"DAY: {item[0]+1}" "," " "f"AMOUNT: SGD{}")
        
        
        #for sublist in diff_list:
            #profit_loss_sgd = sublist*forex
        



        # not done
