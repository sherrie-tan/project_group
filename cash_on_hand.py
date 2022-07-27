import csv
from pathlib import Path
fp = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"


with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)

    for line in reader:
        print(line)

    cash_on_hand_list = [line]
    print(cash_on_hand_list)
