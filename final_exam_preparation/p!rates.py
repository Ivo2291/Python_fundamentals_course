targets_dict = {}
first_command = input()

while first_command != "Sail":
    city, population, gold = first_command.split("||")

    if city not in targets_dict:
        targets_dict[city] = [int(population), int(gold)]

    else:
        targets_dict[city][0] += int(population)
        targets_dict[city][1] += int(gold)

    first_command = input()

second_command = input()

while second_command != "End":
    split_command = second_command.split("=>")
    current_command = split_command[0]
    town = split_command[1]

    if current_command == "Plunder":
        people = int(split_command[2])
        gold = int(split_command[3])

        targets_dict[town][0] -= people
        targets_dict[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if targets_dict[town][0] == 0 or targets_dict[town][1] == 0:
            del targets_dict[town]
            print(f"{town} has been wiped off the map!")

    elif current_command == "Prosper":
        gold = int(split_command[2])

        if gold < 0:
            print(f"Gold added cannot be a negative number!")

        else:
            targets_dict[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {targets_dict[town][1]} gold.")

    second_command = input()

if targets_dict:
    count = len(targets_dict)
    print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")

    for key, value in targets_dict.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

# second_solution

# first_command = input()
# cities = {}
#
# while first_command != "Sail":
#     first_split_command = first_command.split("||")
#     city = first_split_command[0]
#     population = int(first_split_command[1])
#     gold = int(first_split_command[2])
#
#     if city not in cities:
#         cities[city] = {"population": population, "gold": gold}
#
#     else:
#         cities[city]["population"] += population
#         cities[city]["gold"] += gold
#
#     first_command = input()
#
# second_command = input()
#
# while second_command != "End":
#     second_split_command = second_command.split("=>")
#     current_command = second_split_command[0]
#     town = second_split_command[1]
#
#     if current_command == "Plunder":
#         people = int(second_split_command[2])
#         current_gold = int(second_split_command[3])
#
#         cities[town]["population"] -= people
#         cities[town]["gold"] -= current_gold
#         print(f"{town} plundered! {current_gold} gold stolen, {people} citizens killed.")
#
#         if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
#             del cities[town]
#             print(f"{town} has been wiped off the map!")
#
#     elif current_command == "Prosper":
#         current_gold = int(second_split_command[2])
#
#         if current_gold >= 0:
#             cities[town]["gold"] += current_gold
#             print(f"{current_gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
#
#         else:
#             print("Gold added cannot be a negative number!")
#
#     second_command = input()
#
# if len(cities):
#     print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
#     for key, value in cities.items():
#         print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
#
# else:
#     print("Ahoy, Captain! All targets have been plundered and destroyed!")
