import csv

file1 = "Data1.csv"

# Read data from the original CSV file
with open(file1, 'r') as csvfile1:
    csvreader_1 = csv.reader(csvfile1)
    data_2 = list(csvreader_1)

# Update the data by replacing 'A' with 'a'
for row in data_2:
    row[:] = ['A' if cell == 'Arjun'  else cell for cell in row]
    row[:] = ['Bhumi' if cell == 'B'  else cell for cell in row]
    row[:] = ['Male' if cell == 'M' else cell for cell in row]

# Write the updated data to the CSV file
with open(file1, 'w', newline='') as csvfile2:
    csvwriter = csv.writer(csvfile2)
    csvwriter.writerows(data_2)
