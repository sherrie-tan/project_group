import csv
from pathlib import Path
fp = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"


<<<<<<< HEAD
def overhead_function(forex):
    fp = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"

=======
# def overhead_function(forex):
fp = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"
fp_write = Path.cwd()/"summary_report.txt"
fp_write.touch()
>>>>>>> 39287ae9e848a524476af715d8308d5ade0c0580

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
    
    maxValue = max(overheads_list_USD)
    maxValueIndex = overheads_list_USD.index(maxValue)
    print(category_list[maxValueIndex])
    print(maxValue)
    
    # USD_to_SGD = 
    
# highest_overheads_SGD = max(overheads_list_USD)
    

fp = Path.cwd()/"project_group"/"summary_report.txt"
 
with fp.open(mode="a", encoding="UTF-8", newline="") as file:
<<<<<<< HEAD
    file.write(f"\n[HIGHEST OVERHEADS] SALARY EXPENSE {highest_overheads}")
    


    
=======
    file.write(f"\n[HIGHEST OVERHEADS] {category_list[maxValueIndex]}: SGD{maxValue}")

>>>>>>> 39287ae9e848a524476af715d8308d5ade0c0580
