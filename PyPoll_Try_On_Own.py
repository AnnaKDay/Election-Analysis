# Add dependencies
import csv
import os

# Assign a varibale to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to create and save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter
total_votes = 0

# initialize candidates vote counter
votes_1 = 0
votes_2 = 0
votes_3 = 0

# Declare candidate list
candidates = []

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and Print the Header row
    headers = next(file_reader)
 
    # Print each row in the CSV file
    # how does it know that the row variable is referencing rows?
    for row in file_reader:
        #print(row)
        # Increment the total vote count
        total_votes += 1

    # Retrieve and print candadites name
        candidate_name = row[2]
        
        # to only get unique names
        if candidate_name not in candidates:
            candidates.append(candidate_name)

    # Declare candidates
            
        if candidate_name is "Charles Casper Stockham":
            votes_1 += 1
        if candidate_name is "Diana DeGette":
            votes_2 += 1
        if candidate_name is "Raymon Anthony Doane":
            votes_3 += 1
        
# Print the total votes
print(f"There are {total_votes} total votes")

# Print candidates list
print(candidates)

candidate_1 = "Charles Casper Stockham"
candidate_2 = "Diana DeGette"
candidate_3 = "Raymon Anthony Doane" 

# Print votes for each candidate
print(f"{candidate_1} recieved {votes_1} votes.")
print(f"{candidate_2} recieved {votes_2} votes.")
print(f"{candidate_3} recieved {votes_3} votes.")

