import csv
from pathlib import Path
# create file path to read csv file
fp_read = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"
# create file path to write to summary report text file 
fp_write = Path.cwd()/"project_group"/"summary_report.txt"

# create a overheads function with forex as our parameter
"""
This function is used to convert overheads amount from USD to SGD. 

"""
def overhead_function(forex):
    fp_read = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"
    fp_write = Path.cwd()/"project_group"/"summary_report.txt"

# open overheads.csv file to read it 
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        # use next() to skip headers
        next(reader)
        # create a empty list for all data in overheads.csv 
        main_overheads_list = []

# use a for loop to read every line
        for line in reader:
            # use append() to append each line to the empty list
            main_overheads_list.append(line)

    # create 2 empty lists to store the overheads value in USD and expenses' category
        overheads_list_USD = []
        category_list = []
        # use a for loop to go through both empty lists
        for sublist in main_overheads_list:
            # use .append() to obtain the values and categories from main_overheads_list
            overheads_list_USD.append(float(sublist[1]))
            category_list.append((sublist[0]))
            
        # assign maxValue as the variable used to store the highest value in overheads.csv
        maxValue = max(overheads_list_USD)
        # assign maxValueIndex as the variable used to store the name of the overheads that has the 
        # highest value 
        maxValueIndex = overheads_list_USD.index(maxValue)
    

        # assign overheads_SGD as the variable used to store the overheads amount in SGD 
        # by multiplying the value with forex which is contains the currency conversion
        #overheads_SGD = maxValue*forex
        # open the summary_report txt file and use append mode 
        with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
            # use .write() to append the highest overheads category and value to the summary_report txt file
            file.write(f"\n[HIGHEST OVERHEADS] {category_list[maxValueIndex]}: SGD{maxValue}")
 
        


