# Count new salary

# Count the salary of an employed salesperson who earns money
# PLN 2,000 using the shortened version of if. Ask him about his seniority,
# number of hours worked and number of goods sold.

# Initiate base salary
base_salary = 2000

# bonus based on seniority calculation
new_salary = base_salary * 1.1 if (yoexp := int(input("How many years you work here?: "))) > 2 else base_salary * 1.02

# bonus based on sales calculation
new_salary = new_salary * 1.25 if int(input("How much you have sold?: ")) > 30 else new_salary

# bonus based on being active calculation
new_salary = new_salary * 1.08 if int(input("How many hours you work per month?: ")) >= 160 and yoexp > 1 else new_salary * 1.02

# Print output
print(f'Your new salary is {new_salary}.')
