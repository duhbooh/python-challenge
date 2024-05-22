import csv

#file path
file_path = "Resources/election_data.csv"  
output_path = "Analysis/PyPoll_analysis.txt"  

#initialize variables
total_votes = 0
candidates = {}  

#read csv
with open(file_path) as file:
    read_file = csv.reader(file)
    header = next(read_file)

    #loop through data
    for row in read_file:
        total_votes += 1
        candidate_name = row[2]  

        #count candidates/votes
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        #if not in the dictionary, add candidate with one vote
        else:
            candidates[candidate_name] = 1

#percentages and total votes
max_votes = 0
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    #winner
winner = max(candidates, key=candidates.get) 

# results file path
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
