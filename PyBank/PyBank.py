import csv
import os

# Path to find budget_data CSV file in nested Resources folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
prev_month_profit = 0
monthly_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", float("inf")]

# Load and read the CSV file
with open(budget_data_csv) as file:
    csvreader = csv.reader(file, delimiter=",")
    # Skip the header row
    header = next(csvreader) 

    for row in csvreader:
        # Calculate total number of months and net total amount of profit/loss
        total_months += 1
        current_month_profit = int(row[1])
        net_total += current_month_profit

        # Calculate changes in profit/loss if previous month profit is initialized
        if prev_month_profit != 0:
            profit_change = current_month_profit - prev_month_profit
            monthly_changes.append(profit_change)

            # Find greatest increase and decrease
            if profit_change > greatest_increase[1]:
                greatest_increase = [row[0], profit_change]
            if profit_change < greatest_decrease[1]:
                greatest_decrease = [row[0], profit_change]

        # Update previous profit/loss for the next iteration
        prev_month_profit = current_month_profit

# Calculate the average change in profit/loss
average_change = sum(monthly_changes) / len(monthly_changes) if monthly_changes else 0

# Print the analysis report
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

##export the results to a text display file
#with open(analysis_output, "w") as textfile:
   # textfile.write("Financial Analysis\n")
   # textfile.write("----------------------------\n")
   # textfile.write(f"Total Months: {total_months}\n")
   # textfile.write(f"Total: ${total_pro_loss}\n")
   # textfile.write(f"Average Change: ${average_change:.2f}\n")
   # textfile.write(f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})\n")
   # textfile.write(f"Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})\n")
