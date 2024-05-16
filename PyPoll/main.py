#  Modules
import os
import csv

# Creating file path
csvpath = os.path.join("Resources", "election_data.csv")
txtpath = os.path.join("Analysis", "PyPoll.txt")

# Creating lists to store the data
ballots = []
candidates = []
unique_value = []
votes_for_charles = []
votes_for_diana = []
votes_for_raymon = []

# Opening the csvfile
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Calculating data
    for row in csvreader: 
       
      # adding to the ballots
        ballots.append(row[0])

          # adding to the candidates
        candidates.append(row[2])

        # creating separate lists for each candidate
        if (row[2]) == "Charles Casper Stockham":
            votes_for_charles.append(row[0])
        
        if (row[2]) == "Diana DeGette":
            votes_for_diana.append(row[0])

        if (row[2]) == "Raymon Anthony Doane":
            votes_for_raymon.append(row[0])


# For each unique candidate from the election data
for x in candidates:
    if x not in unique_value:
        unique_value.append(x)
        len(ballots)

# Calculating the total number of votes
total_votes = len(ballots)
every_candidate = unique_value

# Calculating the total votes and percentages for every candidate
charles_total = len(votes_for_charles)
charles_percent = charles_total/total_votes
percent_format_charles = "{:.0%}".format(charles_percent)


diana_total = len(votes_for_diana)
diana_percent = diana_total/total_votes
percent_format_diana = "{:.0%}".format(diana_percent)


raymon_total = len(votes_for_raymon)
raymon_percent = raymon_total/total_votes
percent_format_raymon = "{:.0%}".format(raymon_percent)

# Printing the results to the terminal
print("Election Results")
print("------------------------")

print("Total Votes:", total_votes)
print("------------------------")

print(f"Charles Casper Stockham: {percent_format_charles} ({charles_total})")
print(f"Diana DeGette: {percent_format_diana} ({diana_total})")
print(f"Raymon Anthony Doane: {percent_format_raymon} ({raymon_total})")
print("-------------------------")

# Calculating the elections winner
results = {charles_total:"Winner: Charles Casper Stockham",diana_total:"Winner: Diana DeGette",raymon_total:"Winner: Raymon Anthony"}
print(results.get(max(results)))
print("-------------------------")

# export and print the results to .txt file
with open(txtpath, "w" ) as txt_file:

    print("Election Results", file=txt_file)
    print("------------------------", file=txt_file)
    print("Total Votes:", total_votes, file=txt_file)
    print("------------------------", file=txt_file)
    print(f"Charles Casper Stockham: {percent_format_charles} ({charles_total})", file=txt_file)
    print(f"Diana DeGette: {percent_format_diana} ({diana_total})", file=txt_file)
    print(f"Raymon Anthony Doane: {percent_format_raymon} ({raymon_total})", file=txt_file)
    print("-------------------------", file=txt_file)
    results = {charles_total:"Winner: Charles Casper Stockham",diana_total:"Winner: Diana DeGette",raymon_total:"Winner: Raymon Anthony"}
    print(results.get(max(results)), file=txt_file)
    print("-------------------------", file=txt_file)