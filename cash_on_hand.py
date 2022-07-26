import csv
from pathlib import Path
fp = Path.cwd()/"project_group"/"csv reports"/"Cash on Hand.csv"

cash_on_hand_list = []

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)


