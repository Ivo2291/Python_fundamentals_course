number_of_heroes = int(input())
heroes_data_dict = {}

for n in range(number_of_heroes):
    name, hit_points, mana_points = input().split()
    heroes_data_dict[name] = [int(hit_points), int(mana_points)]

command = input()

while command != "End":
    split_command = command.split(" - ")
    current_command = split_command[0]
    hero_name = split_command[1]
    amount = int(split_command[2])

    if current_command == "CastSpell":
        spell_name = split_command[3]

        if heroes_data_dict[hero_name][1] >= amount:
            heroes_data_dict[hero_name][1] -= amount
            print(f"{hero_name} has successfully cast {spell_name}"
                  f" and now has {heroes_data_dict[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif current_command == "TakeDamage":
        attacker = split_command[3]

        if heroes_data_dict[hero_name][0] - amount <= 0:
            del heroes_data_dict[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            heroes_data_dict[hero_name][0] -= amount
            print(f"{hero_name} was hit for {amount} HP by {attacker}"
                  f" and now has {heroes_data_dict[hero_name][0]} HP left!")

    elif current_command == "Recharge":
        if heroes_data_dict[hero_name][1] + amount > 200:
            amount = 200 - heroes_data_dict[hero_name][1]
            heroes_data_dict[hero_name][1] = 200
        else:
            heroes_data_dict[hero_name][1] += amount

        print(f"{hero_name} recharged for {amount} MP!")

    elif current_command == "Heal":
        if heroes_data_dict[hero_name][0] + amount > 100:
            amount = 100 - heroes_data_dict[hero_name][0]
            heroes_data_dict[hero_name][0] = 100
        else:
            heroes_data_dict[hero_name][0] += amount

        print(f"{hero_name} healed for {amount} HP!")

    command = input()

for key, value in heroes_data_dict.items():
    print(f"{key}\n  HP: {value[0]}\n  MP: {value[1]}")

# second_solution

# number = int(input())
# heroes_collection = {}
# for i in range(number):
#     hero_name, hit_points, mana_points = input().split()
#     heroes_collection[hero_name] = {'HP': int(hit_points), 'MP': int(mana_points)}
#
# command = input()
#
# while command != "End":
#     split_command = command.split(" - ")
#     current_command = split_command[0]
#     current_hero = split_command[1]
#
#     if current_command == "CastSpell":
#         MP_needed = int(split_command[2])
#         spell_name = split_command[3]
#
#         if heroes_collection[current_hero]['MP'] < MP_needed:
#             print(f"{current_hero} does not have enough MP to cast {spell_name}!")
#         else:
#             heroes_collection[current_hero]['MP'] -= MP_needed
#             print(f"{current_hero} has successfully cast {spell_name}"
#                   f" and now has {heroes_collection[current_hero]['MP']} MP!")
#
#     elif current_command == "TakeDamage":
#         damage = int(split_command[2])
#         attacker = split_command[3]
#
#         heroes_collection[current_hero]['HP'] -= damage
#
#         if heroes_collection[current_hero]['HP'] > 0:
#             print(f"{current_hero} was hit for {damage} HP by {attacker}"
#                   f" and now has {heroes_collection[current_hero]['HP']} HP left!")
#         else:
#             del heroes_collection[current_hero]
#             print(f"{current_hero} has been killed by {attacker}!")
#
#     elif current_command == "Recharge":
#         amount = int(split_command[2])
#
#         if heroes_collection[current_hero]['MP'] + amount > 200:
#             amount = 200 - heroes_collection[current_hero]['MP']
#
#         heroes_collection[current_hero]['MP'] += amount
#         print(f"{current_hero} recharged for {amount} MP!")
#
#     elif current_command == "Heal":
#         amount = int(split_command[2])
#
#         if heroes_collection[current_hero]['HP'] + amount > 100:
#             amount = 100 - heroes_collection[current_hero]['HP']
#
#         heroes_collection[current_hero]['HP'] += amount
#         print(f"{current_hero} healed for {amount} HP!")
#
#     command = input()
#
# for key, value in heroes_collection.items():
#     print(key)
#     print(f"  HP: {value['HP']}")
#     print(f"  MP: {value['MP']}")
