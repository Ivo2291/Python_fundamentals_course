number_of_lines = int(input())
plants_dict = {}

for number in range(number_of_lines):
    plant, rarity = input().split("<->")
    plants_dict[plant] = {"rarity": rarity, "rating": []}

command = input()

while command != "Exhibition":
    split_command = command.split(": ")
    current_command = split_command[0]

    if current_command == "Rate":
        plant_name, rating = split_command[1].split(" - ")

        if plant_name in plants_dict:
            plants_dict[plant_name]["rating"].append(int(rating))
        else:
            print("error")

    elif current_command == "Update":
        plant_name, new_rarity = split_command[1].split(" - ")

        if plant_name in plants_dict:
            plants_dict[plant_name]["rarity"] = new_rarity
        else:
            print("error")

    elif current_command == "Reset":
        plant_name = split_command[1]

        if plant_name in plants_dict:
            plants_dict[plant_name]["rating"] = []
        else:
            print("error")

    command = input()

for average_rating in plants_dict.values():
    if len(average_rating["rating"]) > 0:
        average_rating["rating"] = sum(average_rating["rating"]) / len(average_rating["rating"])
    else:
        average_rating["rating"] = len(average_rating["rating"])

print("Plants for the exhibition:")

for key, value in plants_dict.items():
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {value['rating']:.2f}")
