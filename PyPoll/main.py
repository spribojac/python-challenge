#%%
# Import the os module to create file paths across operating systems
import os

# Import the csv module to read csv files
import csv

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

# Open the csv file and read it
with open(csvpath) as csvfile:

    # Specify the delimiter and the csv file
    election_data = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    election_header = next(election_data)

    # Initialise lists to store candidate names and votes
    candidate_names = []
    candidate_votes = []

    # Initialise variable for total votes
    total_votes = 0

    # Loop through the rows
    for row in election_data:

        # Total the number of votes
        total_votes += 1

        # Set the candidate name
        candidate_name = row[2]

        # Check if the candidate name is already in the list
        if candidate_name in candidate_names: # If candidate name in row[2] is the same as the stored candidate name before then...
            candidate_index = candidate_names.index(candidate_name) # Go to the index of the candidate name in the list and return the numeric value of that position
            candidate_votes[candidate_index] += 1 # In the corresponding index in the candidate votes list add 1
        else:
            candidate_names.append(candidate_name) # Add the new name to the candidate name list
            candidate_votes.append(1) # Add one to the votes for the candidate in the candidate votes list

    # Find the winning candidate
    max_votes = max(candidate_votes) # Use max function on the candidate votes list to find max value
    max_position = candidate_votes.index(max_votes) # Find the index position of that vote number in the candidate votes list and store
    winner = candidate_names[max_position] # In the candidates name use the index to find the corresponding name

# Print the election results analysis
print(f"Election Results")
print(f"---------------------")
print(f"Total Votes:, {total_votes}")
print(f"---------------------")

# For each name in the range of candidate names
for name in range(len(candidate_names)):
    candidate = candidate_names[name] # Find the candidate name
    votes = candidate_votes[name] # Find the number of votes

    # Print the leaderboard and for each candidate do a calculation of percentage of votes to 3dp
    print(f"{candidate}: {votes} votes ({votes/total_votes * 100:.3f}% of total)") 

print(f"---------------------")
print(f"Winning Candidate: " + winner)
print(f"---------------------")

# Export results as a text file
pathout = os.path.join('..', 'PyPoll', 'election_results.txt')
with open(pathout, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("---------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("---------------------\n")
    for name in range(len(candidate_names)):
        candidate = candidate_names[name]
        votes = candidate_votes[name]
        percentage = (votes / total_votes) * 100
        txt_file.write(f"{candidate}: {votes} votes ({percentage:.3f}% of total)\n")
    txt_file.write("---------------------\n")
    txt_file.write(f"Winning Candidate: {winner}\n")
    txt_file.write("---------------------\n")
# %%
