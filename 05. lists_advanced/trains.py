wagons_number = int(input())
train = [0 for wagon in range(wagons_number)]

command = input()

while command != "End":
    commands_list = command.split()
    current_command = commands_list[0]

    if current_command == "add":
        people_count = int(commands_list[1])
        train[-1] += people_count

    if current_command == "insert":
        position = int(commands_list[1])
        people_count = int(commands_list[2])
        train[position] += people_count

    if current_command == "leave":
        position = int(commands_list[1])
        people_count = int(commands_list[2])
        train[position] -= people_count

    command = input()

print(train)
