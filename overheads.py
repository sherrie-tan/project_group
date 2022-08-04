import csv
from pathlib import Path
import re

# creating the file path to read csv file
fp_read = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"
# creating the file path to write summary report text file 
fp_write = Path.cwd()/"project_group"/"summary_report.txt"

# creating an overheads function with forex as our parameter
"""
This function is used to convert overheads amount from USD to SGD. 

"""
def overhead_function(forex):
    fp_read = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"
    fp_write = Path.cwd()/"project_group"/"summary_report.txt"

# opening overheads.csv file in read mode to read it
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        # using next() to skip headers
        next(reader)
        # creating an empty list for all data in overheads.csv 
        main_overheads_list = []

# using for loop to read every line
        for line in reader:
            # using .append() to append each line to the empty list
            main_overheads_list.append(line)

    # creating 2 empty lists to store the overheads value in USD and expenses category
        overheads_list_USD = []
        category_list = []
        # using for loop to go through both empty lists
        for sublist in main_overheads_list:
            # using .append() to obtain the values and categories from main_overheads_list
            overheads_list_USD.append(float(sublist[1]))
            category_list.append((sublist[0]))
            
        # assigning maxValue as the variable used to store the highest value in overheads.csv
        maxValue = max(overheads_list_USD)
        # assigning maxValueIndex as the variable used to store the name of the overheads 
        # that has the highest value 
        maxValueIndex = overheads_list_USD.index(maxValue)
    
        overheads_list = []
        with fp_write.open(mode="r", encoding="UTF-8") as file:
            api = file.read()
            overheads_list.append(api)

        for info, value in enumerate(overheads_list):
            forex = re.search(pattern="SGD.+\d", string=value)
            forex = forex.group()
            forex = float(forex[3:10])

        # assigning overheads_SGD as the variable used to store the overheads amount in SGD 
        # by multiplying the value with forex which contains the currency conversion
        # overheads_SGD = maxValue*forex
        # opening the summary_report txt file in append mode 
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
            # using .write() to append the highest overheads category and value to the summary_report txt file
            file.write(f"\n[HIGHEST OVERHEADS] {category_list[maxValueIndex]}: SGD{maxValue*forex}")
 
        


