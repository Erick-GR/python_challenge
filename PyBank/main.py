import csv

fileName = "budget_data.csv"
newFile = "financial_analysis.txt"
net_tot = 0

with open(fileName, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    rows = []
    for row in csv_reader:
        rows.append(row)

cont = len(rows)
sum_prom = 0
greatest_in = 0
greatest_de = 0

for i in range(cont):
    net_tot += int(rows[i][1])
    if i+1 < cont:
        dif = int(rows[i+1][1]) - int(rows[i][1])
        sum_prom += dif
        if dif > 0 and dif > greatest_in:
            g_in_date = rows[i+1][0]
            greatest_in = dif
        if dif < 0 and dif < greatest_de:
            g_de_date = rows[i+1][0]
            greatest_de = dif

ave_change = round(sum_prom/(cont-1), 2)

with open(newFile, 'w') as nFile:
    nFile.write(f"Financial Analysis\n")
    nFile.write("--------------------------\n")
    nFile.write(f"There are {cont} months in the dataset\n")
    nFile.write(f"The net total amount of Profit/Losses is: ${net_tot}\n")
    nFile.write(f"Average Change: ${ave_change}\n")
    nFile.write(f"Greatest Increase in Profits: {g_in_date} (${greatest_in})\n")
    nFile.write(f"Greatest Decrease in Profits: {g_de_date} (${greatest_de})\n")

print("Financial Analysis")
print("--------------------------")
print(f"There are {cont} months in the dataset")
print(f"The net total amount of Profit/Losses is: ${net_tot}")
print(f"Average Change: ${ave_change}")
print(f"Greatest Increase in Profits: {g_in_date} (${greatest_in})")
print(f"Greatest Decrease in Profits: {g_de_date} (${greatest_de})")
