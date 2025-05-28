# Module 8 - Write table data to csv file

# TASK DESCRIPTION
# Use what you have learned about CSV files to create a new file
# containing some data, and then read in the second program
# all collected information

# Import libraries
import csv


# Testing data


# Declare function
with open('cars.csv', mode='w', newline='') as csvfile:
    c_names = ['Name', 'time_to_100', 'speed_record']
    writer = csv.DictWriter(csvfile, fieldnames=c_names)
    writer.writeheader()
    writer.writerow({c_names[0]: 'Hennessey Venom F5', c_names[1]: 2.6, c_names[2]: 484})
    writer.writerow({c_names[0]: 'SSC Tuatara', c_names[1]: 2.5, c_names[2]: 460})
    writer.writerow({c_names[0]: 'Koenigsegg Agera RS', c_names[1]: 3.1, c_names[2]: 457})
    writer.writerow({c_names[0]: 'Koenigsegg One 1', c_names[1]: 2.6, c_names[2]: 450})


with open('cars.csv', newline='') as csvfile:
    c_names = ['Name', 'time_to_100', 'speed_record']
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        print(row)

# Tests


# Print output message
