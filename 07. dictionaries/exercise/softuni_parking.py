number_of_commands = int(input())
parking_info_dict = {}

for number in range(number_of_commands):
    current_command = input().split()
    command = current_command[0]
    username = current_command[1]

    if command == "register":
        license_plate_number = current_command[2]

        if username not in parking_info_dict:
            parking_info_dict[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

    elif command == "unregister":

        if username not in parking_info_dict:
            print(f"ERROR: user {username} not found")

        else:
            del parking_info_dict[username]
            print(f"{username} unregistered successfully")

for user, license_plate in parking_info_dict.items():
    print(f"{user} => {license_plate}")
