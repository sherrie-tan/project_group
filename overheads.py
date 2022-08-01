import csv
from pathlib import Path
fp = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"
fp_write = Path.cwd()/"summary_report.txt"
fp_write.touch()

# def overhead_function(forex):
fp = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"
fp_write = Path.cwd()/"summary_report.txt"
fp_write.touch()

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    main_overheads_list = []

    for line in reader:
         main_overheads_list.append(line)
    # print((main_overheads_list))

    overheads_list_USD = []
    category_list = []
    for sublist in main_overheads_list:
        overheads_list_USD.append(float(sublist[1]))
        category_list.append((sublist[0]))
    
    
    print(max(overheads_list_USD))
    print((category_list))
    
# highest_overheads = max(overheads_list_USD)
# highest_overheads_SGD = max(overheads_list_USD)
    

# fp = Path.cwd()/"project_group"/"summary_report.txt"
 
# with fp.open(mode="a", encoding="UTF-8", newline="") as file:
    # file.write(f"[HIGHEST OVERHEADS] SALARY EXPENSE SGD{highest_overheads}")
