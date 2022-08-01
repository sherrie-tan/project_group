import csv
from pathlib import Path

fp = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
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
    

    print(max(overheads_list_USD))
    print(max(category_list))
    

    

# fp = Path.cwd()/"project_group"/"summary_report.txt"
 
# with fp.open(mode="a", encoding="UTF-8", newline="") as file:
    # writer = csv.writer(file)
    # writer.writerow(["[HIGHEST OVERHEADS]"])

