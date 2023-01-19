text = input()
courses = {}

while ":" in text:
    (name, student_id, course) = text.split(":")

    if course not in courses:
        courses[course] = {}

    courses[course][student_id] = name

    text = input()

searched_course = text.replace("_", " ")

if searched_course in courses:
    for info in courses[searched_course]:
        print(f"{courses[searched_course][info]} - {info}")
