chest_treasure = input().split("|")
command = input()

while command != "Yohoho!":
    split_command = command.split()
    current_command = split_command[0]

    if current_command == "Loot":
        other_items = split_command[1:]
        items_list = [item for item in other_items if item not in chest_treasure]

        while items_list:
            chest_treasure.insert(0, items_list[0])
            items_list.pop(0)

    elif current_command == "Drop":
        index = int(split_command[1])

        if 0 <= index < len(chest_treasure):
            popped_item = chest_treasure.pop(index)
            chest_treasure.append(popped_item)

    elif current_command == "Steal":
        count = int(split_command[1])

        if count >= len(chest_treasure):
            print(", ".join(chest_treasure))
            print("Failed treasure hunt.")
            chest_treasure.clear()

        else:
            popped_list = []

            for i in range(count):
                current_item = chest_treasure.pop(-1)
                popped_list.append(current_item)
            popped_list.reverse()
            print(", ".join(popped_list))

    command = input()

length_of_chest = "".join(chest_treasure)

if length_of_chest:
    average_gain = len(length_of_chest) / len(chest_treasure)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
