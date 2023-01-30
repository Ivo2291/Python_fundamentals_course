journal_with_items = input().split(", ")
command = input()

while command != "Craft!":
    split_command = command.split(" - ")
    current_command = split_command[0]
    item = split_command[1]

    if current_command == "Collect":
        if item not in journal_with_items:
            journal_with_items.append(item)

    elif current_command == "Drop":
        if item in journal_with_items:
            journal_with_items.remove(item)

    elif current_command == "Combine Items":
        split_item = item.split(":")
        old_item = split_item[0]
        new_item = split_item[1]
        if old_item in journal_with_items:
            journal_with_items.insert(journal_with_items.index(old_item) + 1, new_item)

    elif current_command == "Renew":
        if item in journal_with_items:
            element_index = journal_with_items.index(item)
            popped_item = journal_with_items.pop(element_index)
            journal_with_items.append(popped_item)

    command = input()

joined_items = ", ".join(journal_with_items)

print(joined_items)
