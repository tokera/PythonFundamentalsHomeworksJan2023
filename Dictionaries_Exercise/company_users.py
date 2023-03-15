line = input()
companies = {}
while line != "End":
    company_name, employee_id = line.split(" -> ")
    if company_name not in companies:
        companies[company_name] = []
        companies[company_name].append(employee_id)
    else:
        if employee_id not in companies[company_name]:
            companies[company_name].append(employee_id)

    line = input()

for company, employees in companies.items():
    print(f"{company}")
    for employee in employees:
        print(f"-- {employee}")
