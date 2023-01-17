#imports
import csv 
import os

#file path
Bank_CSV = os.path.join("Resources", "budget_data.csv")

months = 0
profitloss = []
changeamt = []
changedate = []
changecalc = 0.0
first = 0.0
second = 0.0
    
with open(Bank_CSV) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
 
    #find net total of profit/loss
    for row in csv_reader:
        #count months
        months+=1
        
        #add profit/loss to list
        profitloss.append(int(row[1]))
        
        #calulate change month to month
        first = (int(row[1]))
        changeamt.append(first - second)
        second = (int(row[1]))
        
        #add dates to list
        changedate.append(row[0])
        
        
#remove first data points, no change on first row        
changeamt.remove(1088983)
changedate.remove('Jan-10')

#pull index values for days with greatest increase/decrease
maxindex = changeamt.index(max(changeamt))
minindex = changeamt.index(min(changeamt))


print("Total months: ", months)
print("Total profits: $", sum(profitloss))
print("Average change: $", sum(changeamt)/len(changeamt))
print("Greatest increase in profits: ", changedate[maxindex], max(changeamt))
print("Greatest decrease in profits: ", changedate[minindex], min(changeamt))


with open("Analysis/PyBank_Analysis.txt", 'w') as f:
    f.write("Total months:  86, Total profits: $ 22564198, Average change: $ -8311.105882352942, Greatest increase in profits:  Aug-16 1862002, Greatest decrease in profits:  Feb-14 -1825558")