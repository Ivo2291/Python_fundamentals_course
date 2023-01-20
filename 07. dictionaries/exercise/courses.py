courses_information = input()
courses_info_dict = {}

while courses_information != "end":
    course_name, student_name = courses_information.split(" : ")

    if course_name not in courses_info_dict:
        courses_info_dict[course_name] = []
    courses_info_dict[course_name].append(student_name)

    courses_information = input()

for current_course in courses_info_dict.keys():
    print(f"{current_course}: {len(courses_info_dict[current_course])}")

    for student in courses_info_dict[current_course]:
        print(f"-- {student}")
