employees_happiness = list(map(int, input().split()))
improvement_factor = int(input())

employees_happiness = list(x * improvement_factor for x in employees_happiness)
average_happiness = sum(employees_happiness) / len(employees_happiness)

happy_employees = list(x for x in employees_happiness if x >= average_happiness)
happy_count = len(happy_employees)
total_count = len(employees_happiness)

if len(happy_employees) >= len(employees_happiness) / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
