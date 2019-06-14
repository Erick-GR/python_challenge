import csv
import operator

fileName = "election_data.csv"
newFile = "election_results.txt"

with open(fileName, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    rows = []
    for row in csv_reader:
        rows.append(row)

t_votes = len(rows)
candidates = {}

for v in rows:
    if v[2] not in candidates:
        candidates[v[2]] = 1
    else:
        candidates[v[2]] += 1

winner = max(candidates.items(), key=operator.itemgetter(1))[0]

with open(newFile, 'w') as nFile:
    nFile.write("Election Results\n")
    nFile.write("--------------------\n")
    nFile.write(f"Total Votes: {t_votes}\n")
    nFile.write("--------------------\n")
    for v in candidates:
        percentage = candidates[v]/t_votes*100
        nFile.write(f"{v}: {percentage:.3f}% ({candidates[v]})\n")
    nFile.write("--------------------\n")
    nFile.write(f"Winner: {winner}\n")
    nFile.write("--------------------\n")

print("Election Results")
print("--------------------")
print(f"Total Votes: {t_votes}")
print("--------------------")
for v in candidates:
    percentage = candidates[v]/t_votes*100
    print(f"{v}: {percentage:.3f}% ({candidates[v]})")
print("--------------------")
print(f"Winner: {winner}")
print("--------------------")
