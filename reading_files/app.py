employee_file = open("C:/Users/veeti/OneDrive - Luksia/html 2/python/reading_files/employee.txt", "r")

for employee in employee_file.readlines():
    print(employee)
# print(employee_file.readlines()[2])

employee_file.close()