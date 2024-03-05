import csv


# Add New Line

with open("SomeText.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Yeni", "Setir"])


# Read The File

with open("SomeText.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
