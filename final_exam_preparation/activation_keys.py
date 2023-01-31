raw_activation_key = input()
command = input()

while command != "Generate":
    split_command = command.split(">>>")
    current_command = split_command[0]

    if current_command == "Contains":
        substring = split_command[1]

        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif current_command == "Flip":
        additional_command = split_command[1]
        start_index = int(split_command[2])
        end_index = int(split_command[3])

        if additional_command == "Upper":
            upper_letters = raw_activation_key[start_index:end_index].upper()
            raw_activation_key = raw_activation_key.replace(raw_activation_key[start_index:end_index], upper_letters)

        elif additional_command == "Lower":
            lower_letters = raw_activation_key[start_index:end_index].lower()
            raw_activation_key = raw_activation_key.replace(raw_activation_key[start_index:end_index], lower_letters)

        print(raw_activation_key)

    elif current_command == "Slice":
        start_index = int(split_command[1])
        end_index = int(split_command[2])

        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]

        print(raw_activation_key)

    command = input()

print(f"Your activation key is: {raw_activation_key}")
