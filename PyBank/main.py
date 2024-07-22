import csv
import os

#file path 
file_path = "Resources/budget_data.csv"
output_path = "Analysis/budget_analysis.txt"
 
#initialize variables
total_months = 0 
net_total = 0
monthly_changes = []
greatest_increase = ["",0]
greatest_decrease = ["",float("inf")]
prev_amount = 0
 
#read csv
with open(file_path) as file: 
    read_file = csv.reader(file)
    header = next(read_file)

    #loop through data
    for row in read_file:
        total_months +=1
        net_total +=int(row[1])
    
    #calculate monthly changes
        change = int(row[1]) - prev_amount
        prev_amount = int(row[1])
        monthly_changes += [change]

    #greatest increase
        if change > greatest_increase[1]:
            greatest_increase = [row[0], change]

    #greatest decrease
        if change < greatest_decrease[1]:
            greatest_decrease = [row[0], change]

#average monthly change
average_change = sum(monthly_changes) / len(monthly_changes)

results = (
f"financial analysis:\n"
f"------------------\n"
f"months: {total_months}\n"
f"total: {net_total}\n"
f"Average Change: ${average_change:.2f}\n"
f"greatest_increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"greatest_decrease: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

#printing the results to the file
print(results)
with open(output_path,"w") as output_file:  
    output_file.write(results)


















