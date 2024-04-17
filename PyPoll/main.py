#import required modules 
import os
import csv

#path to find election_data CSV file in nested Resources folder
election_data_csv=os.path.join('..', 'Resources', 'election_data_csv')

#define variables 
total_votes = 0
candidates={}
winner=""
winning_votes=0

#read the election_data CSV file
with open(election_data_csv, 'r') as file:
    csvreader=csv.reader(file,delimiter=",")

    #skip the header row
    next(csvreader)

    #evaluate each row in the CSV file
    for row in csvreader:
        total_votes+=1
        candidates=row[2]

        #count the votes per candidate
        if candidate in candidates:
            candidates[candidate]+=1
        else:
            candidates[candidate]=1

    #calculate percentage of votes per candidate
    results={}
    for candidate, votes in candidate.items():
        percent=(votes/total_votes)*100
        result[candidate]=(percent, votes)

        #identify the winner
        if votes>winning_votes:
            winning_votes=votes
            winner=candidate

#Print results
print("Election Results")
print("----------------")
print(f"Total Votes:{total_votes}")
print("----------------")

for candidate, (percentage,votes) in results.items{}:
    #verify formula to make string of response text
    #print(f"{candidate}":"{percent}", "{votes}")


    



    

