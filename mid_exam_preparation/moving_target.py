targets = list(map(int, input().split()))
command = input()

while command != "End":
    split_command = command.split()
    current_command = split_command[0]
    index = int(split_command[1])
    value = int(split_command[2])

    if current_command == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif current_command == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif current_command == "Strike":
        if 0 <= index - value and index + value < len(targets):
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")

    command = input()

targets = list(map(str, targets))

print("|".join(targets))
