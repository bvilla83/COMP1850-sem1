# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]

reports = {}

with open("student_data.csv", "r") as data:
    next(data)
    for line in data:
        row = line.split(',')
        average = int(row[2]) + int(row[3]) + int(row[4]) / 3
        reports[row[1]] = average

# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3

with open("report.txt", "w") as file:
    for (k, v) in reports.items():
        file.write(f"{k}'s average grade: {v:.2f}\n")


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f