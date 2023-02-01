stops_info = input()
command = input()

while command != "Travel":
    split_command = command.split(":")
    current_command = split_command[0]

    if current_command == "Add Stop":
        index = int(split_command[1])
        string = split_command[2]

        if 0 <= index < len(stops_info):
            stops_info = stops_info[:index] + string + stops_info[index:]
        print(stops_info)

    elif current_command == "Remove Stop":
        start_index = int(split_command[1])
        end_index = int(split_command[2])

        if 0 <= start_index < len(stops_info) and 0 <= end_index < len(stops_info):
            # for i in range(end_index, start_index - 1, -1): That works too
            #     stops = stops.replace(stops[i], "", 1)

            stops_info = stops_info[:start_index] + stops_info[end_index + 1:]
        print(stops_info)

    elif current_command == "Switch":
        old_string = split_command[1]
        new_string = split_command[2]

        if old_string in stops_info:
            stops_info = stops_info.replace(old_string, new_string)
        print(stops_info)

    command = input()

print(f"Ready for world tour! Planned stops: {stops_info}")
