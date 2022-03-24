# Add dependencies
import csv
import os

# Assign a varibale to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to create and save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter
total_votes = 0

# Declare candidate list
candidates = []

# Declare an empty dictionary to hold votes for each candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

    # Retrieve and print candidates name
        candidate_name = row[2]
        
        # to only get unique names
        if candidate_name not in candidates:
            candidates.append(candidate_name)

            # Add list of candidates to the dictonary and set value equal to zero
            candidate_votes[candidate_name] = 0

        # Add a vote everytime that candidate's name pops up
        candidate_votes[candidate_name] += 1
        
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate_name}: received {vote_percentage: .1f}% of the total vote")

        print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

# Print the total votes
# print(f"There are {total_votes} total votes")

# Print candidates list
# print(candidates)

# Print candidate vote dictionary
# print(candidate_votes)

#print(f"{winning_candidate} won the vote at {winning_count} votes, which is {winning_percentage: .1f}% of the total votes")

winning_candidate_summary = (f"--------------------\n"f"Winner: {winning_candidate}\n"f"Winning Vote Count: {winning_count:,}\n"f"Winning Percentage: {winning_percentage: .1f}%\n"f"---------------------\n")
print(winning_candidate_summary)