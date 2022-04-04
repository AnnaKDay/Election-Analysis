# election-analysis
Polling analysis automation with Python

## Overview
This analysis endeavors to calculate and organize election results for the relevant election commission to review. The results have been coded to print to a separate text file so that the commission can see a summary of the results including turnout by county, largest county turnout, percentage of votes for each candidate, and finally, the winning candidate.
## Election-Audit Results
- In three counties (Jefferson, Denver, and Arapahoe), a total of 369,711 votes were cast for three candidates (Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane)
- Jefferson county had a turnout of 38,855 votes, comprising 10.5% of the total votes cast. Denver had nearly ten times the voter turnout at 306,055 votes, making up 82.8% of the total votes cast. Arapahoe had the least amount of votes at 24,801 votes, and 6.7% of the total votes cast.
- Denver overwhelmingly had the largest turnout and the largest percentage of votes cast out of the total votes from all three counties. It is apparent that Denver's voting power in the election can outweigh the voting power of Jefferson county and Arapahoe county, even if the two counties were united.
- Candidate Charles Casper Stockham recieved 85,213 votes of the total 369,711, at 23.0% of the total votes. Candidate Diana DeGette recieved 272,892 votes, comprising 73.8% of the total votes. Candidate Raymon Anthony Doane recieved 11,606 votes, at 3.1% of the total votes cast. 
- Diana DeGette won in a landslide with 272,892 votes, at 73.8% of total votes. She won by 40 percentage points from the second most popular candidate.
## Election-Audit Summary
This code can be adapted easily to audit other elections, as long as there is an availble CSV file with the appropriate information, in the appropriate order. If the CSV files of other elections are organized by Ballot Id, County, and Candidate, all that needs to be changed to run this code is the file path of the CSV file.

If the CSV is missing any of this information, contains additional information, or is organized in a different order, then the code needs to be modified further to fit. Mainly, in the following section: