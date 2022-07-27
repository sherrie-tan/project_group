import csv
from pathlib import Path
fp = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"
print(fp)
print(fp.exists())

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)

    for line in reader:
        print(line)


