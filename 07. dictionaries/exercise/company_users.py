command = input()
company_data = {}

while command != "End":
    company_name, employees_id = command.split(" -> ")

    if company_name not in company_data:
        company_data[company_name] = []

    if employees_id not in company_data[company_name]:
        company_data[company_name].append(employees_id)

    command = input()

for current_company in company_data.keys():
    print(current_company)

    for employee in company_data[current_company]:
        print(f"-- {employee}")
