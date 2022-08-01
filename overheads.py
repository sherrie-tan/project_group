import csv
from pathlib import Path

def overhead_function():
    fp = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"

    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
     reader = csv.reader(file)
     next(reader)
     data = list(reader)

     print(data)


    

# fp = Path.cwd()/"project_group"/"summary_report.txt"
 
# with fp.open(mode="a", encoding="UTF-8", newline="") as file:
    # writer = csv.writer(file)
    # writer.writerow(["[HIGHEST OVERHEADS]"])

