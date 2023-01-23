number_of_lines = int(input())
students_info_dict = {}

for number in range(number_of_lines):
    name = input()
    grade = float(input())

    if name not in students_info_dict:
        students_info_dict[name] = []
    students_info_dict[name].append(grade)

best_students_dict = {}

for student, grades in students_info_dict.items():
    average_grade = sum(grades) / len(grades)

    if average_grade >= 4.5:
        best_students_dict[student] = average_grade

for student_name, student_grade in best_students_dict.items():
    print(f"{student_name} -> {student_grade:.2f}")
