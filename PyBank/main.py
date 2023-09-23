#Import the CSV file & define the path for PyBank
import os
import csv

#define input and output for the files
input_file = "budget_data.csv"
output_filename = "budget_results.txt"

csvpath =os.path.join("PyBank","Resources","budget_data.csv")

#Intialize all the variables 
total_months = 0
total_profit_loss = 0 
previous_profit_loss = 0
changes_profit_loss = []
dates = []
greatest_increase = {"date":"","amount":0}
greatest_decrease = {"date":"","amount":0}

#Open up the CSV & set delimiter 
with open (csvpath ,encoding='UTF-8') as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=",")

    #Skip the header of the file
    csv_header = next(csvreader)

    #start looping through the file
    for row in csvreader:
        #pull out date and the profit/loss & ensure profit loss is an integer
        data = row[0]
        profit_loss = int(row[1])

        total_months += 1
        total_profit_loss += profit_loss

        #calculate changes & dates
        if total_months > 1:
            changes_profit_loss_int = profit_loss - previous_profit_loss
            changes_profit_loss.append(changes_profit_loss_int)
            dates.extend(dates)

            #check within the above for increases and decreases 
            if changes_profit_loss_int > greatest_increase ["amount"]:
                greatest_increase["date"] = dates
                greatest_increase["amount"]= changes_profit_loss_int
            elif changes_profit_loss_int < greatest_decrease ["amount"]:
                greatest_decrease["date"] = dates
                greatest_decrease["amount"]= changes_profit_loss_int
       
        #update profit/loss for the next loop
        previous_profit_loss = profit_loss
#average the changes
average_change = sum(changes_profit_loss)/len(changes_profit_loss)

#place results in folder and file
output_directory = "python-challenge/PyBank/analysis"
output_filename = "analysis"

#print the above results
print("Financial Analysis")
print("---------------------")
print(f"Total Months:{total_months}")
print(f"Total:${total_profit_loss}")
print(f"Average Change:${average_change:.2f}")
print(f"Greatest Increase in Profits:{greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits:{greatest_decrease['date']} (${greatest_decrease['amount']})")

output_file= "PyBank/analysis/analysis.txt"

#add everything to a txt file 
with open(output_file,"w") as txtfile:
    txtfile.write("Financial Analysis")
    txtfile.write("---------------------")
    txtfile.write(f"Total Months:{total_months}")
    txtfile.write(f"Total:${total_profit_loss}")
    txtfile.write(f"Average Change:${average_change:.2f}")
    txtfile.write(f"Greatest Increase in Profits:{greatest_increase['date']} (${greatest_increase['amount']})")
    txtfile.write(f"Greatest Decrease in Profits:{greatest_decrease['date']} (${greatest_decrease['amount']})")

