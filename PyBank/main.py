import os
import csv
file = os.path.join('..', 'Resources', 'budget_data.csv')
# start csv file
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    # prepares variables and start conditions 
    total_month = []
    profit = []
    change_profit = []
        # read in each row of data 
    for row in csvreader:
        total_month.append(row[0])
        profit.append(int(row[1]))
    for c in range(len(profit)-1):
        change_profit.append(profit[c+1]-profit[c])
                      
#Develop the max and min 
increase = max(change_profit)
decrease = min(change_profit)
 
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(total_month)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {total_month[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {total_month[month_decrease]} (${(str(decrease))})")  

#generate output lines
output = os.path.join(".", 'output.txt')
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(total_month)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {total_month[month_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {total_month[month_decrease]} (${(str(decrease))})")