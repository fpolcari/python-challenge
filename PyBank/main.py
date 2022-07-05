"""In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
You will be given a financial dataset called budget_data.csv.
The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""

import os # need that to join the file path
import csv # needed to handle the csv files

budgetData = os.path.join("Resources", "budget_data.csv") # budget_data.csv has a header

# create a file to hold the output of the Budget Data Analysis
outputFile = os.path.join("analysis", "FinancialAnalysis.txt")

# variables
totalMonths = 0  #initialize the total months to 0
NetTotal = 0  # initialize the Net Total to 0
ProfitLoss = [] # initialize the list of monthly profit/loss
months = [] # initialize the list of months

# read the original CSV file and grab the necessary data (
with open(budgetData, "r", encoding="utf-8") as Data:
    # create the reader object
    csvreader = (csv.reader(Data, delimiter=","))

    header = next(csvreader)
    # move to the first row
    firstRow = next(csvreader)

    # Iincrement the count of the total months
    totalMonths += 1

    # add on the Net Total Amount of profit & losses over the entire period
            # Profit/Losses is in index 1
    NetTotal += float(firstRow[1])

    # establish the previous profit/loss
        # profit/loss is in index 1
    previousProfitLoss = float(firstRow[1])

    for row in csvreader:
        # Iincrement the count of the total months
        totalMonths += 1

        # add on the Net Total Amount of profit & losses over the entire period
            # Profit/Losses is in index 1
        NetTotal += float(row[1])

        # calculate the changes in "Profit/Losses" over the entire period
        netChange = float(row[1]) - previousProfitLoss
        ProfitLoss.append(netChange)

        # add the first month that a changed occurred
            # month is in index 0
        months.append(row[0])

        # update the previous profit/loss
        previousProfitLoss = float(row[1])

# calculate the average net change per month
averageChange = sum(ProfitLoss) / len(ProfitLoss)

greatestIncrease = [months[0], ProfitLoss[0]] # holds the month and the value of the greatest increase in profit
greatestDecrease = [months[0], ProfitLoss[0]] # holds the month and the value of the greatest decrease in profit

# use loop to calculate the index of the greatest and least monthly change
for PL in range(len(ProfitLoss)):
    # calculate the greatest increase and decrease
    if(ProfitLoss[PL] > greatestIncrease[1]):
        # if the value is greater than the greatest increase, that value becomes the new greatest increase
        greatestIncrease[1] = ProfitLoss[PL]
        # update the month
        greatestIncrease[0] = months[PL]


    if(ProfitLoss[PL] < greatestDecrease[1]):
        # if the value is less than the greatest decrease, that value becomes the new greatest decrease
        greatestDecrease[1] = ProfitLoss[PL]
        # update the month
        greatestDecrease[0] = months[PL]

#start generating the output
output = (
    f"\nFinancial Analysis \n"
    f"------------------------------------ \n"
    f"Total Months = {totalMonths} \n"
    f"Total: ${NetTotal:.0f} \n"
    f"Average Change: ${averageChange:.2f} \n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]:.0f}) \n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]:.0f}) \n"
    )

# print the output to the console / terminal
print(output)

# export the output variable to the output text file
with open(outputFile, "w") as textfile:
    textfile.write(output)