#imports
import csv 
import os

#file path
Bank_CSV = os.path.join("Resources", "budget_data.csv")

with open(Bank_CSV) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

months = len(list(csv_reader))
print(months)