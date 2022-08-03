import csv
from pathlib import Path
fp_read = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"
fp_write = Path.cwd()/"project_group"/"summary_report.txt"

def overhead_function(forex):
    fp_read = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"
    fp_write = Path.cwd()/"project_group"/"summary_report.txt"


    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        main_overheads_list = []

        for line in reader:
            main_overheads_list.append(line)

    
        overheads_list_USD = []
        category_list = []
        for sublist in main_overheads_list:
            overheads_list_USD.append(float(sublist[1]))
            category_list.append((sublist[0]))
        print(overheads_list_USD)
        print(category_list)

    maxValue = max(overheads_list_USD)
    maxValueIndex = overheads_list_USD.index(maxValue)
    print(category_list[maxValueIndex])
    print(maxValue)

    
    #overheads_SGD = maxValue*forex
    
 
    


