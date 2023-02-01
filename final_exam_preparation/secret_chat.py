message = input()
command = input()

while command != "Reveal":
    split_command = command.split(":|:")
    current_command = split_command[0]

    if current_command == "InsertSpace":
        index = int(split_command[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif current_command == "Reverse":
        substring = split_command[1]

        if substring in message:
            reversed_string = reversed(substring)
            message = message.replace(substring, "", 1)
            message += "".join(reversed_string)
            print(message)

        else:
            print("error")

    elif current_command == "ChangeAll":
        substring = split_command[1]
        replacement = split_command[2]

        message = message.replace(substring, replacement)
        print(message)

    command = input()

print(f"You have a new text message: {message}")
