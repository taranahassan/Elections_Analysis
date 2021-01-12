#Importing dependencies
import csv
import os

#Assign variable to load a file from a path.
file_to_load = 'Resources/election_results.csv'
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#initializing total vote counter
total_votes = 0
#initializing new list for candidate
candidate_options = []
#declaring empty dictionary
candidate_votes = {}
#variables for winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open election results and read file
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Read the header row
    headers= next(file_reader)
    #Print each row in the csv file
    for row in file_reader:
        #increase count by 1
        total_votes += 1
        #print candidate name from each row
        candidate_name = row[2]
        #if candidate does not match existing candidate add to list
        if candidate_name not in candidate_options:
            #add candidate name to list
            candidate_options.append(candidate_name)
            #counting candidate votes
            candidate_votes[candidate_name] = 0
        #increasing by one
        candidate_votes[candidate_name] += 1

#saving results on text file
with open(file_to_save, "w") as txt_file:
    #printing final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #saving final vote count to text file
    txt_file.write(election_results)

    #find the percentage of votes for each candidate by looping though the counts
    #looping through candidate list
    for candidate_name in candidate_votes:
        #get total count of votes for each candidate
        votes = candidate_votes[candidate_name]
        #calculate percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100
        #print out each candidate's name, vote count and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #save results to text file
        txt_file.write(candidate_results)
        #find winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
    #print out each name, vote count and percentage of votes
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)
    #save winning results to text file
    txt_file.write(winning_candidate_summary)