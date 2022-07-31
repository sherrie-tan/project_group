import csv
from pathlib import Path
fp = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"


fp = Path.cwd()/"project_group"/"summary_report.txt"
 
with fp.open(mode="a", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["HIGHEST OVERHEADS"])

