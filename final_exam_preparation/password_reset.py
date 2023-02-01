password = input()
command = input()

while command != "Done":
    split_command = command.split()
    current_command = split_command[0]

    if current_command == "TakeOdd":
        raw_password = ""
        for char in range(1, len(password), 2):
            raw_password += password[char]
        password = raw_password
        print(password)

    elif current_command == "Cut":
        index = int(split_command[1])
        length = int(split_command[2])

        cut_substring = password[index:index + length]
        password = password.replace(cut_substring, "", 1)
        print(password)

    elif current_command == "Substitute":
        substring = split_command[1]
        substitute = split_command[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")
