# Data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 4. Total number of votes each candidate received
# 5. Percentage of votes each candidate won
# 6. The winner of th election based on popular vote

import csv
import os

# CSV Path: Resources\election_results_mod.csv
    
    # Assign a variable for the file to load and the path

#file_to_load = "Resources\election_results_mod.csv"
#file_to_load = os.path.join("Resources", "election_results_mod.csv")

        # Open the election results and read the file
#election_data = open(file_to_load, "r")
#with open(file_to_load) as election_data:
    #print(election_data)
        # To do: perform analysis

        #Close the file.
#election_data.close()

        # Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

        # Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")

        #Write some data to the file
#outfile.write("Hello World")

        #close file
#outfile.close()

        #Cleaner Version
file_to_save = os.path.join("analysis", "test.txt")

with open(file_to_save, "w") as txt_file:
    txt_file.write("Hello World")
    #note: when writing text in, if you have the txt open in open file tab above, this will not show the updated changes, you will have to exit out and reopen from the Workspace 
    #also, exit from that open file before running python code to make it more simple, for now
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson, ")
    #txt_file.write("Arapahoe, Denver, Jefferson")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

skill_drill = os.path.join("analysis", "skill_drill.txt")

with open(skill_drill, "w") as txt_file:
    txt_file.write("Counties in the Election\n----------------\nArapahoe\nDenver\nJefferson")
