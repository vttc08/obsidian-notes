import os
import shutil
import csv


# Reading CSV
with open('readfile.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        video_id = row['id']
        video_title = row['title']
# assuming the csv is formatted with 2 columns id and title

# Writing CSV
with open('writefile.csv', 'w', newline='', encoding='utf-8') as csvfile: # open the csv file
    fieldnames = ['col 1', 'col 2'] # define number of columns
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader() 
    # Iterate through a list of variables 
    variable = []
    for item, item2 in variable: # loop through variables and write items in corresponding column
        writer.writerow({'col 1': item, 'col 2': item2})
