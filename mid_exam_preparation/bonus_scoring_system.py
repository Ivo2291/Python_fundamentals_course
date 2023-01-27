from math import ceil

number_of_students = int(input())
lectures_count = int(input())
additional_bonus = int(input())
max_bonus = 0
best_student_attendance = 0

for student in range(number_of_students):
    attendance = int(input())
    total_bonus = attendance / lectures_count * (5 + additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        best_student_attendance = attendance

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {best_student_attendance} lectures.")
