employees = input().split()
employees = list(map(int, employees))
factor = int(input())
average = sum(employees) / len(employees)

happy_employees = list(filter(lambda emp: emp >= average, employees))

if len(happy_employees) >= len(employees) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")


# second_solution

employees_happiness = input().split()
factor = int(input())
employees_list = []
filtered = []

# employees_happiness = list(map(lambda x: int(x) * factor, employees_happiness))
for employee in employees_happiness:
    employees_list.append(int(employee) * factor)

# filtered_happiness = list(
#     filter(lambda x: x >= sum(employees_happiness) / len(employees_happiness), employees_happiness))
for happiness in employees_list:
    if happiness >= sum(employees_list) / len(employees_list):
        filtered.append(happiness)

happy_employees = len(filtered)
total_employees = len(employees_happiness)

if happy_employees >= total_employees / 2:
    print(f"Score: {happy_employees}/{total_employees}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{total_employees}. Employees are not happy!")
