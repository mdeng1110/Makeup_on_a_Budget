import csv
rows = []
with open("kvdbeauty_data.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        rows.append(row)
print(rows)