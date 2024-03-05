import csv


# Write new csv file

with open("NewFile.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows([["Yeni", "Setir"], ["New", "Line"], ["Task", "Completed"]])
