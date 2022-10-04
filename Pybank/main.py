# Import os module
import os
# Import csv module
import csv
# Import statistics
import statistics
# Create a file path to the data
file_path = os.path.join('..','Resources','budget_data.csv')
#initialize variables
total_months = 0
total_amount = 0
greatestincrease = 0
greatestdecrease = 0
bestmonth= ''
worstmonth = ''
monthly_changes = []
change = []
#Open and read CSV file
with open(file_path) as file:
    csvreader = csv.reader(file, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        #find the total months and total profits/losses
        total_months += 1
        amount = row[1]
        total_amount += int(amount)
        #find the greatest increase
        if int(row[1]) > greatestincrease:
            bestmonth = (row[0])
            greatestincrease = int(row[1])
        #find the greatest decrease
        elif int(row[1]) < greatestdecrease:
            worstmonth = (row[0])
            greatestdecrease = int(row[1])
        change.append(int(row[1]))
#calculating monthly changes
    for i in range(len(change)-1):
        changeamount = (change[i+1] - change[i])
        monthly_changes.append(changeamount) 
avg_change =  statistics.mean(monthly_changes)
 
   
#print analysis result   
print('Financial Analysis')
print('----------------------------')
print(f'Total Months:' + str(total_months))
print('Total:' + str(total_amount))
print('Average Change: $' + str(avg_change))
print('Greatest Increase in Profits:'+ str(bestmonth)+ ' ' + str(greatestincrease))
print('Greatest decrease in Profits:'+ str(worstmonth)+ ' ' + str(greatestdecrease))

# now write this to an output file
f = open("financial_analysis.txt", "w")
f.write('Financial Analysis')
f.write('----------------------------')
f.write(f'Total Months:' + str(total_months))
f.write('Total:' + str(total_amount))
f.write('Average Change: $' + str(avg_change))
f.write('Greatest Increase in Profits:'+ str(bestmonth)+ ' ' + str(greatestincrease))
f.write('Greatest decrease in Profits:'+ str(worstmonth)+ ' ' + str(greatestdecrease))
