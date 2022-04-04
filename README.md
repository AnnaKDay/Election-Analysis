# election-analysis
Polling analysis automation with Python

## Overview
This analysis endeavors to calculate and organize election results for the relevant election commission to review. The results have been coded to print to a separate text file so that the commission can see a summary of the results including turnout by county, largest county turnout, percentage of votes for each candidate, and finally, the winning candidate.
## Election-Audit Results
- In three counties (Jefferson, Denver, and Arapahoe), a total of 369,711 votes were cast for three candidates (Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane)
```# For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
```
- Jefferson county had a turnout of 38,855 votes, comprising 10.5% of the total votes cast. Denver had nearly ten times the voter turnout at 306,055 votes, making up 82.8% of the total votes cast. Arapahoe had the least amount of votes at 24,801 votes, and 6.7% of the total votes cast.
``` # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
    
        # 6b: Retrieve the county vote count.
        county_total_votes = county_votes.get(county_name)
        
        # 6c: Calculate the percentage of votes for the county.
        county_vote_percent = float(county_total_votes) / float(total_votes) * 100
        
         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {county_vote_percent:.1f}% ({county_total_votes:,})\n"f"\n")
            
        print(county_results)
        
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_total_votes > highest_turnout_votes) and (county_vote_percent > county_turnout_percent):
            highest_turnout_votes = county_total_votes
            county_highest_turnout = county_name
            county_turnout_percent = county_vote_percent
```
- Denver overwhelmingly had the largest turnout and the largest percentage of votes cast out of the total votes from all three counties. It is apparent that Denver's voting power in the election can outweigh the voting power of Jefferson county and Arapahoe county, even if the two counties were united.
```# 7: Print the county with the largest turnout to the terminal.
    highest_turnout_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {county_highest_turnout}\n"
        f"County Vote Count: {highest_turnout_votes:,}\n"
        f"County Percentage: {county_turnout_percent:.1f}%\n"
        f"-------------------------\n")
        
    print(highest_turnout_summary)
```
- Candidate Charles Casper Stockham recieved 85,213 votes of the total 369,711, at 23.0% of the total votes. Candidate Diana DeGette recieved 272,892 votes, comprising 73.8% of the total votes. Candidate Raymon Anthony Doane recieved 11,606 votes, at 3.1% of the total votes cast. 
```
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
```
- Diana DeGette won in a landslide with 272,892 votes, at 73.8% of total votes. She won by 40 percentage points from the second most popular candidate.
```# Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
```
## Election-Audit Summary
This code can be adapted easily to audit other elections, as long as there is an availble CSV file with the appropriate information, in the appropriate order. If the CSV files of other elections are organized by Ballot Id, County, and Candidate, all that needs to be changed to run this code is the file path of the CSV file:
```# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
```
The path within the parentheses would need to be modified according to the folder and then the name of the CSV file.

#### Otherwise:

If the CSV is missing any of this information, contains additional information, or is organized in a different order, then the code needs to be modified further to fit. Mainly, in the following section:
```# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name= row[1]
```
The information needs to be read from the appropriate rows, so, if row index 2 is not the placement of the candidates name, the index needs to be changed to fit the CSV file. Likewise, if there is additional information, that needs to be read and extracted by assigned a variable and finding the row and referencing its index position. If there is missing information, maybe the election commission going forward does not want to include counties for some reason, that variable can be removed from here and every part of the code it appears in.


