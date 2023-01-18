import os
import csv

TotalMonths = 0
InitialProfit = 0
TotalProfit = 0

MonthlyChange = []
AverageChange = []
MaxIncreases = ["", 0]
MaxDecreases = ["", 99999999999]

#Create path to csv file
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        #The total number of months included in the dataset
        TotalMonths += 1
        
        #The net total amount of "Profit/Losses" over the entire period
        TotalProfit = TotalProfit + int(row[1])

        #The changes in "Profit/Losses" over the entire period
        next = int(row[1])

        #Caculate the profit changes
        ProfitChange = next - InitialProfit
        MonthlyChange.append(ProfitChange)
        InitialProfit = int(row[1]) 

        date = (row[0])
        
        #The greatest increase in profits (date and amount) over the entire period
        if (ProfitChange > MaxIncreases[1]):
           MaxIncreases[0] = date
           MaxIncreases[1] = ProfitChange
           
        #The greatest decrease in profits (date and amount) over the entire period
        if (ProfitChange < MaxDecreases[1]):
           MaxDecreases[0] = date
           MaxDecreases[1] = ProfitChange

    #the average of those changes
    AverageChange = round((sum(MonthlyChange[1:]) / (TotalMonths-1)), 2)   

    #printing the results
    print("------------------------------------------------")
    print("Financial Analysis")
    print("------------------------------------------------")
    print(f"Total Months: {TotalMonths}")
    print(f"Total: $ {TotalProfit}")
    print(f"Average: $ {AverageChange}")
    print(f"Greatest Increase in Profits: $ {MaxIncreases[0]}, ($ {MaxIncreases[1]})")
    print(f"Greatest Decrease in Profits: $ {MaxDecreases[0]}, ($ {MaxDecreases[1]})")
    print("------------------------------------------------")   

text_file = ('..', 'analysis', 'PyBank_text_file.txt')

with open(text_file, "w") as textfile:
    textfile.write("------------------------------------------------\n")
    textfile.write("Financial Analysis" + "\n")
    textfile.write("------------------------------------------------\n")  
    textfile.write(f"Total Months: {TotalMonths}\n")
    textfile.write(f"Total: $ {TotalProfit}\n")
    textfile.write(f"Average: $ {AverageChange}\n")
    textfile.write(f"Greatest Increase in Profits: $ {MaxIncreases[0]}, ($ {MaxIncreases[1]})\n")
    textfile.write(f"Greatest Decrease in Profits: $ {MaxDecreases[0]}, ($ {MaxDecreases[1]})\n")
    textfile.write("------------------------------------------------\n")  
