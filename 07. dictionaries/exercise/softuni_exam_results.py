user_name_statistics = {}
submissions = {}
command = input()

while command != "exam finished":
    split_command = command.split("-")

    if split_command[1] == "banned":
        name = split_command[0]
        del user_name_statistics[name]

    else:
        username, language, points = split_command
        points = int(points)

        if username in user_name_statistics:
            if user_name_statistics[username] < points:
                user_name_statistics[username] = points
        else:
            user_name_statistics[username] = points

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1

    command = input()

print("Results:")
for user, user_points in user_name_statistics.items():
    print(f"{user} | {user_points}")

print("Submissions:")
for current_language, submission in submissions.items():
    print(f"{current_language} - {submission}")
