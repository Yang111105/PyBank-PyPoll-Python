import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

# Create lists to store election_data
vote_list = [] # List for every vote     

# Read election data and store in new lists created
with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    # print(f'CSV Header: {csv_header}')

    for row in csvreader:   
        # Add each vote to list
        vote_list.append(row[2])
        
        # Find out the total number of votes
        total_votes = len(vote_list)

    # Find out unique candidate and vote counts    
    candidate_count = {c:vote_list.count(c) for c in set(vote_list)}
    
    # Find out the winner
    winner = max(set(vote_list),key=vote_list.count)


    #-----------Print the summary--------------------------------------------------------------------------------
    print(f'Election Results\n---------------------------\nTotal Votes: {total_votes}\n---------------------------')
    
    # Loop through the dict and print vote details for each candidates. Percentage is calculated here
    for candidate,count in sorted(candidate_count.items(),key=lambda x: x[1], reverse=True):
        percent = round(count/total_votes*100,3)
        print(f'{candidate} {"%.3f"%percent}% ({count})') 
    
    print(f'--------------------------- \nWinner: {winner}\n---------------------------')


#--------------Create text output file to export---------------------------------------------------------------- 

# Below lines were used to create the intial "analysis" folder 
# path_dir = os.getcwd()
# directory = "analysis"
# os.mkdir(os.path.join(path_dir, directory))
output_summary_file = os.path.join("analysis","output_election_summary.txt")

with open(output_summary_file, "w", newline="") as datafile:

# Write the header row
    datafile.write('Election Results')

# Write in summary rows
    datafile.write(f'\n---------------------------\nTotal Votes: {total_votes}\n---------------------------\n')

    for candidate,count in sorted(candidate_count.items(),key=lambda x: x[1], reverse=True):
        percent = round(count/total_votes*100,3)
        datafile.write(f'{candidate} {"%.3f"%percent}% ({count})\n') 
    
    datafile.write(f'---------------------------\nWinner: {winner}\n---------------------------')