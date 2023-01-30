first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())
answered_students_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
needed_time = 0

while students_count > 0:
    needed_time += 1

    if needed_time % 4 == 0:
        continue
    else:
        students_count -= answered_students_per_hour

print(f"Time needed: {needed_time}h.")
