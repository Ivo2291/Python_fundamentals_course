encrypted_message = input()
command = input()

while command != "Decode":
    split_command = command.split("|")
    current_command = split_command[0]

    if current_command == "Move":
        number_of_letters = int(split_command[1])

        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]

    elif current_command == "Insert":
        index = int(split_command[1])
        value = split_command[2]

        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif current_command == "ChangeAll":
        substring = split_command[1]
        replacement = split_command[2]

        encrypted_message = encrypted_message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {encrypted_message}")
