lessons = input().split(", ")
command = input().split(":")

while command[0] != "course start":
    current_command = command[0]
    lesson_title = command[1]

    if current_command == "Add":
        if lesson_title not in lessons:
            lessons.append(lesson_title)

    elif current_command == "Insert":
        index = int(command[2])
        if lesson_title not in lessons:
            lessons.insert(index, lesson_title)

    elif current_command == "Remove":
        if lesson_title in lessons:
            lessons.remove(lesson_title)

    elif current_command == "Swap":
        second_lesson_title = command[2]
        if lesson_title in lessons and second_lesson_title in lessons:
            first_index = int(lessons.index(lesson_title))
            second_index = int(lessons.index(second_lesson_title))
            lessons[first_index], lessons[second_index] = lessons[second_index], lessons[first_index]

    elif current_command == "Exercise":
        if lesson_title in lessons and "Exercise" not in lesson_title:
            lessons.append(f"{lesson_title}-Exercise")
        elif lesson_title not in lessons:
            lessons.append(lesson_title)
            lessons.append(f"{lesson_title}-Exercise")

    command = input().split(":")

for i in range(len(lessons)):
    print(f"{i + 1}.{lessons[i]}")
