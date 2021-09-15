import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")
# print (budget_csv)

# Lists to store budget_data
mm_yy = []      # List for dates
pnl = []        # List for montly pnl

# Read budget_data
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) 
 
    total_pnl=0 # Set initial total pnl value for calculation

    # Loop through rows in csvreader
    for row in csvreader:

        # Add dates & pnl to lists
        mm_yy.append(row[0])
        pnl.append(row[1])
        
         # Find out total number of months
        total_months = len(mm_yy)
        
        # Add up all P&L
        total_pnl += int(row[1])    

   
    # Calculate monthly changes and find out the greatest increase/decrease
    total_pnl_change = 0 # Set initial net pnl change value
    greatest_increase = 0 # Set initial greatest pnl increase value
    greatest_decrease = 0 # Set initial greatest pnl decrease value


    # Loop through pnl list to calculate monthly changes and compare
    for month in range(1, total_months):
        
        # Calculate monthly change
        monthly_change = int(pnl[month]) - int(pnl[month-1])

        # Calculate total pnl change
        total_pnl_change += monthly_change

        # Find out the greatese increase/decrease
        # Find out the months for greatest pnl changes in the date list
        if (monthly_change > greatest_increase):
            greatest_increase = monthly_change
            greatest_increase_month = mm_yy[month]
        elif (monthly_change < greatest_decrease):
            greatest_decrease = monthly_change
            greatest_decrease_month = mm_yy[month]

    # Calculate the average pnl change
    average_pnl_change =  round(total_pnl_change/(total_months-1),2)

   
    #---------------------Print the summary------------------------------------------------------------ 
    print(f'Financial Analysis')
    print('----------------------------------')
    print(f'Total Months: {str(total_months)}') 
    print (f'Total: ${int(total_pnl)}')
    print (f'Average Change: ${average_pnl_change}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')  


#-------------------------Create text file export------------------------------------------------------
# Set variable for output text file
path_dir = os.getcwd()
directory = "analysis"
os.mkdir(os.path.join(path_dir, directory))
output_summary_file = os.path.join("analysis","output_budget_summary.txt")

#  Open the output file
with open(output_summary_file, "w", newline="") as datafile:

# Write the header row
    datafile.write('Financial Analysis')

# Write in summary rows
    datafile.write(f'\n------------------------------------------------')   
    datafile.write(f'\nTotal Months: {str(total_months)}')    
    datafile.write(f'\nTotal: ${int(total_pnl)}')
    datafile.write(f'\nAverage Change: ${average_pnl_change}')   
    datafile.write(f'\nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    datafile.write(f'\nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')         