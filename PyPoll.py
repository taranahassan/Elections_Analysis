# The data we need to retrieve
# 1.Total count of votes cast
# 2.Complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of the election based on popular votes

import csv
import os

#Assign variable for file to load and the path.
file_to_load = 'Resources/election_results.csv'
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open election results and read file
with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers= next(file_reader)
    print(headers)