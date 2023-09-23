import os
import csv

#define paths for the data
input_file="PyPoll/Resources/election_data.csv"
output_file = "PyPoll/analysis/election_results.txt"

#define varibales
total_votes=0
candidate_votes = {}

#open csv and create the loop
with open(input_file,newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader) #skip the header row 

    for row in csvreader:
        total_votes +=1
        canidate = row[2]
        candidate_votes[total_votes]= candidate_votes.get(canidate, 0) + 1
#calculate the winner
winner = max(candidate_votes,key=candidate_votes.get)

#add election results to the terminal
print("Elections Results")
print("--------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")

#calculate all the candidate stats 
for canidate, votes in candidate_votes.items():
    percentage = (votes/total_votes)*100 
    print(f"{canidate}:{percentage:.3f}% ({votes})")

#print to terminal
print("--------------")
print(f"Winner:{winner}")
print("--------------")

#add everything to a txt file 
with open(output_file,"w") as txtfile:
    txtfile.write("Elections Results\n")
    txtfile.write("--------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-----------------------\n")

    #recalculate the same candiate stats from above and print to txt file
    #calculate all the candidate stats 
    for canidate, votes in candidate_votes.items():
     percentage = (votes/total_votes)*100 
     print(f"{canidate}:{percentage:.3f}% ({votes})")
    
    print("--------------\n")
    print(f"Winner:{winner}\n")
    print("--------------\n")

print("Complete")
