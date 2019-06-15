import csv
from datetime import datetime
import us_state_abbrev

fileName = "employee_data.csv"
newFile = "new_employee_data.csv"

id = []
name = []
dob = []
ssn = []
state = []

with open(fileName, 'r', newline='') as csvFile:
    csvR = csv.reader(csvFile, delimiter=',')
    next(csvR)

    for row in csvR:
        id.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])

t_length = len(id)
fName = []
lName = []

for i in range(t_length):
    split_name = name[i].split()
    fName.append(split_name[0])
    lName.append(split_name[1])

    newDate = datetime.strptime(dob[i], '%Y-%m-%d')
    dob[i] = newDate.strftime('%m/%d/%Y')

    split_ssn = ssn[i].split("-")
    for s in range(2):
        split_ssn[s] = len(split_ssn[s]) * '*'
    ssn[i] = '-'.join(str(r) for r in split_ssn)

    state[i] = us_state_abbrev.us_state_abbrev[state[i]]

z = zip(id, fName, lName, dob, ssn, state)

with open(newFile, 'w', newline='') as csvFile:
    csvW = csv.writer(csvFile)

    csvW.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    csvW.writerows(z)
