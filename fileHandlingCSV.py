import csv

# Open the file in write mode
p = open("demo.csv", "w", newline='')

# Create a CSV writer object
empdata = csv.writer(p)

# Write the header row
empdata.writerow(["Empid", "Emp Name", "Salary"])

# Loop to get data for 3 employees
for i in range(3):
    # try:
        empid = int(input("Enter ID: "))
        empname = input("Enter Name: ")
        empsalary = int(input("Enter Salary: "))
        
        # Create a list with employee data
        empinfo = [empid, empname, empsalary]
        
        # Write the employee data to the CSV file
        empdata.writerow(empinfo)
    # except ValueError:
    #     print("Please enter valid inputs for ID and Salary (numeric values).")
    #     break

# Close the file
p.close()