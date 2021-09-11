import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# Lists to store budget_data
mm_yy = []
pnl = []

# Read budget_data and store as new lists created
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add date
        mm_yy.append(row[0])

        # Find out the total number of months in the list
        total_months = len(mm_yy)
 
        # Add pnl
        pnl.append(row[1])

        # Add up all P&L
        net_pnl = 0
        for pnl in len(pnl):
            net_pnl += pnl 

        
        # Determine percent of review left to 2 decimal places
        percent = round(int(row[6]) / int(row[5]), 2)
        review_percent.append(percent)

        # Get length of the course to just a number
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))

# Zip lists together
cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)