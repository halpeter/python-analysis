import os
import csv

budget_csv = os.path.join('resources','budget_data.csv')

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    #define variables
    total = 0
    total_months = 0
    maximum = 0
    minimum = 0
    first_row = 1
    running_total = 0
    #difference = []

    for row in csvreader:
        #The total number of months included in the dataset
        total_months = total_months + 1

        #The net total amount of "Profit/Losses" over the entire period
        profit_loss = int(row[1])
        total = total + profit_loss
        
        #Calculate the changes in "Profit/Losses" over the entire period
        #difference.append()
        if first_row != 1:
            running_total = running_total + (int(row[1]) - first_value)
            first_value = int(row[1])

        if first_row == 1:
            first_value = int(row[1])
            first_row = 2

        #The greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > int(maximum):
            maximum = int(row[1])
            maximum_date = str(row[0])
        
        #The greatest decrease in losses (date and amount) over the entire period
        if int(row[1]) < int(minimum):
            minimum = int(row[1])
            minimum_date = str(row[0])

    #calculate the average of the changes in profit/losses
    average = "{:.2f}".format(running_total / (total_months - 1))

    #Print info
    print("Financial Analysis")
    print("---------------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: {maximum_date} (${maximum})')
    print(f'Greatest Increase in Profits: {minimum_date} (${minimum})')

#export a text file with the results