import csv
with open("people.csv", "r") as f:
	reader = csv.DictReader(f)
	for row in reader:
		print(row)