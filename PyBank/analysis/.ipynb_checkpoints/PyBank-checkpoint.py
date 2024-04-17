import os
import csv

#path to find budget_data CSV file in nested Resources folder
budget_data_csv= os.path.join('..', 'Resources', 'budget_data.csv')

#define variables
total_months=0
net_total=0
prev_profit_loss=0
profit_changes= []
greatest_increase=["", 0]
greatest_decrease=["", 999999999999999999]

#load and read the CSV file
with open('budget_data.csv') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    #skip the header row
    csv_header=next(csvreader)

    #loop through each row in csv file
    for row in csvreader:
        #calculate total number of months
        total_months+=1

        #calculate net total amount of profit/loss
        net_total+=int(row[1])

        #calculate changes in profit/loss and store in list
        if total_months>1:
            change=int(row[1])-prev_profit_loss
            profit_changes.append(change)

    #update previous profit/loss for the next iteration
    prev_profit_loss=int(row[1])

    #find the greatest inrease in profit
    if change>greatest_increase[1]:
        greatest_increase-[row[0],change]

    #find the greatest decrease in profit
    if change<greatest_decrease[1]:
        greatest_decrease=[row[0],change]

#calculate the average change in profit/loss
average_change=sum(profit_changes)/len(profit_changes)

#print the analysis report
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

#export the results to a text display file
with open('financial_analysis.txt', 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
