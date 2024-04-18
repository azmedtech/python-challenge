#import required modules 
import os
import csv

#path to find election_data CSV file in nested Resources folder
election_data_csv = os.path.join("Resources","election_data.csv")

#define variables 
total_votes = 0
candidates={}
winner=""
winning_votes=0

#read the election_data CSV file
with open(election_data_csv) as file:
    csvreader=csv.reader(file,delimiter=",")

    #skip the header row
    next(csvreader)

    #evaluate each row in the CSV file
    for row in csvreader:
        total_votes+=1

        #count the votes per candidate
        if row[2] in candidates:
             candidates[row[2]] += 1
        else:
             candidates[row[2]] = 1

    #calculate percentage of votes per candidate
    results={}

    winning_votes = candidates['Charles Casper Stockham']

    for candidate, votes in candidates.items():
        percent=votes/total_votes
        results[candidate]=(percent, votes)

        #identify the winner
        if votes>winning_votes:
            winning_votes=votes
            winner=candidate

#print resuls of analysis        
print("Election Results")    
print("----------------")
print(f"Total Votes:{total_votes}")
print("----------------")

for candidate, (percentage,votes) in results.items():
    #print(f"{candidate}:  {percent}%, ({votes})")
    print(f"{candidate}: {percentage:.2%} ({votes})")

print("----------------")
print(f"Winner: {winner}")

#export the results to a text display file
#with open('financial_analysis.txt', 'w') as textfile:
   # textfile.write("Financial Analysis\n")
   # textfile.write("----------------------------\n")
   # textfile.write(f"Total Months: {total_months}\n")
   # textfile.write(f"Total: ${total_pro_loss}\n")
   # textfile.write(f"Average Change: ${average_change:.2f}\n")
   # textfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
   # textfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
    



    

