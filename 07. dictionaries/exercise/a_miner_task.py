resource = input()
items_dictionary = {}

while resource != "stop":
    quantity = int(input())

    if resource not in items_dictionary:
        items_dictionary[resource] = []
    items_dictionary[resource].append(quantity)

    resource = input()

for key, value in items_dictionary.items():
    print(f"{key} -> {sum(value)}")
