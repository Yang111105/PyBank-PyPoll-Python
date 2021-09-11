import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")
print (budget_csv)

# Lists to store budget_data
mm_yy = []
pnl = []
pnl_change = []

# Read budget_data and store as new lists created
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add date
        mm_yy.append(row[0])

        # Find out the total number of months in the list
        total_months = len(mm_yy)
        print(f'Total Months: {str(total_months)}')
 
        # Add pnl
        pnl.append(row[1])

        # Add up all P&L
        net_pnl = 0
        for pnl in len(pnl):
            net_pnl += pnl 

        print (f'Total: {float(net_pnl)}')


        # Calculate pnl changes and store to a new list
        for month in range (total_months):
            monthly_change = pnl[month+1] - pnl[month]
            pnl_change.append(monthly_change)
            print(pnl_change)


        # Find out the greatese increase
        greatest_increase = pnl_change[0]
        for month in range (total_months):
            if (pnl_change[month+1] > greatest_increase):
                greatest_increase = pnl_change[month+1]
        
        greatest_increase_month = pnl_change.index(greatest_increase)
  
        print(f'Greatest Increase in Profits: {mm_yy[greatest_increase_month]} {greatest_increase}')


         # Find out the greatese decrease
        greatest_decrease = pnl_list[0]
        for month in range (total_months):
            if (pnl_change[month+1] < greatest_decrease):
                greatest_decrease = pnl_change[month+1]

        greatest_decrease_month = pnl_change.index(greatest_decrease)   
        
        print(f'Greatest Decrease in Profits: {mm_yy[greatest_decrease_month]} {greatest_decrease}')      