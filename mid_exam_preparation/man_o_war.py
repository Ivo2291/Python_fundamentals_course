pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
maximum_health_capacity = int(input())
command = input()
there_is_no_winner = True

while command != "Retire":
    split_command = command.split()
    current_command = split_command[0]

    if current_command == "Fire":
        index = int(split_command[1])
        pirate_ship_damage = int(split_command[2])
        if 0 <= index < len(warship):
            warship[index] -= pirate_ship_damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                there_is_no_winner = False
                break

    elif current_command == "Defend":
        start_index = int(split_command[1])
        end_index = int(split_command[2])
        warship_damage = int(split_command[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for section in range(start_index, end_index + 1):
                pirate_ship[section] -= warship_damage
                if pirate_ship[section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    there_is_no_winner = False
                    break

    elif current_command == "Repair":
        index = int(split_command[1])
        health = int(split_command[2])
        if 0 <= index < len(pirate_ship):
            if pirate_ship[index] + health > maximum_health_capacity:
                health = maximum_health_capacity - pirate_ship[index]
            pirate_ship[index] += health

    elif current_command == "Status":
        min_health = maximum_health_capacity * 0.2
        repair_counter_list = [i for i in pirate_ship if i < min_health]
        print(f"{len(repair_counter_list)} sections need repair.")

    command = input()

if there_is_no_winner:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
