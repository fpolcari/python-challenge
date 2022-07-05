"""
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote
"""
# import the csv and os modules
import csv
import os

# load the file to read poll data
electionData = os.path.join("Resources", "election_data.csv") # election_data.csv has a header

# output file location for the survey
outputFile = os.path.join("analysis", "ElectionResults.txt")

# variables
totalVotes = 0 # variable that holds the total number of votes
Candidates = [] # list that holds the candidates
NumberOfVotes = {} # dictionary that will hold the number of votes for each candidate
winningCount = 0 # variable will hold the winning count
winningCandidate = "" # variable to hold the winning candidate

# read the CSV file
with open(electionData) as voteData:
    # create the csv 
    csvreader = csv.reader(voteData)

    # read the header
    header = next(csvreader)

    # row will be lists
        # index 0 is the Ballot ID
        # index 1 is the County
        # index 2 is the Candidate (voter's choice)

    # loop for each row
    for row in csvreader:
        # add on to the total votes
        totalVotes += 1

        # check to see if the candidates are listed
        if row[2] not in Candidates:
            # if the candidates is not in the list of Candidates, add them
            Candidates.append(row[2])

            # add the value to the dictionary as well
            # the instance you get a vote you start your count
            # start the count at 1 for the candidate votes
            NumberOfVotes[row[2]] = 1

        else:
            # the Candidate(s) is in the list
            # add a vote to their count
            NumberOfVotes[row[2]] += 1

voteOutput = ""

for Candidates in NumberOfVotes:
    # retrieve the vote count and the percentage of the votes
    votes = NumberOfVotes.get(Candidates)
    votePCT = (float(votes) / float (totalVotes)) * 100.00

    # the plus equals is there so we can add on new lines to the vote output
    voteOutput += f"\n{Candidates}: {votePCT:.3f}% ({votes})\n"

    # compare the votes to the winning count
    if votes > winningCount:
        # update the votes to be the new winning count
        winningCount = votes
        # update the winning candidate
        winningCandidate = Candidates

winningCandidateOutput = f"Winner: {winningCandidate}\n"

# create an output variable to hold the output
output = (

        f"\nElection Results\n\n"
        f"--------------------------\n\n"
        f"Total Votes: {totalVotes:}\n\n"
        f"--------------------------\n"
        f"{voteOutput} \n"
        f"--------------------------\n"
        f"{winningCandidateOutput}"
        f"--------------------------\n"

    )

# displays the output to the console also known as the terminal
print(output)

# print the results and export the data to a text file
with open(outputFile, "w") as textFile:
    # write the output to the text file
    textFile.write(output)

