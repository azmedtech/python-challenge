import os
import csv

#path to find budget_data CSV file in nested Resources folder
budget_data_csv= os.path.join("Resources", "budget_data.csv")

#load and read the CSV file
with open(budget_data_csv) as file:
    csvreader=csv.reader(file, delimiter=",")

    #skip the header row
    next(csvreader)

    #define variables
    total_months=0
    pro_loss=0
    total_pro_loss=0
    prev_pro_loss=0
    profit_changes= []
    dates=[]

    #loop through each row in csv file
    for row in csvreader:
        #calculate total number of months
        total_months = total_months + 1

        #calculate total amount of profit/loss
        amount_change = int(row[1])
        pro_loss = pro_loss + amount_change

        #calculate changes in profit/loss and store in list
        #identify corresponding dates and store in list
        if prev_pro_loss != 0:
            change=amount_change-prev_pro_loss
            profit_changes.append(row[0])
            dates.append(row[0])
            total_pro_loss = total_pro_loss + change

        #update previous profit/loss for the next iteration
        prev_pro_loss=amount_change

    #calculate the average change in profit/loss
    average_change=total_pro_loss/(total_months-1)

#find the greatest inrease in profit
greatest_increase=max(profit_changes)
greatest_decrease=min(profit_changes)
date_greatest_increase=dates[profit_changes.index(greatest_increase)]
date_greatest_decrease=dates[profit_changes.index(greatest_decrease)]

#print the analysis report
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${pro_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})")

##export the results to a text display file
#with open(analysis_output, "w") as textfile:
   # textfile.write("Financial Analysis\n")
   # textfile.write("----------------------------\n")
   # textfile.write(f"Total Months: {total_months}\n")
   # textfile.write(f"Total: ${total_pro_loss}\n")
   # textfile.write(f"Average Change: ${average_change:.2f}\n")
   # textfile.write(f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})\n")
   # textfile.write(f"Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})\n")
