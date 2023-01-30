groceries_list = input().split("!")
command = input()

while command != "Go Shopping!":
    split_command = command.split()
    current_command = split_command[0]
    item = split_command[1]

    if current_command == "Urgent":
        if item not in groceries_list:
            groceries_list.insert(0, item)

    elif current_command == "Unnecessary":
        if item in groceries_list:
            groceries_list.remove(item)

    elif current_command == "Correct":
        new_item = split_command[2]
        if item in groceries_list:

            for i in range(len(groceries_list)):
                if groceries_list[i] == item:
                    groceries_list[i] = new_item

    elif current_command == "Rearrange":
        if item in groceries_list:
            groceries_list.remove(item)
            groceries_list.append(item)

    command = input()

print(", ".join(groceries_list))
