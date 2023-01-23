data = input()
phonebook = {}

while "-" in data:
    name, phone_number = data.split("-")

    if name not in phonebook:
        phonebook[name] = phone_number
    phonebook[name] = phone_number

    data = input()

for person in range(int(data)):
    searched_name = input()

    if searched_name not in phonebook:
        print(f"Contact {searched_name} does not exist.")
    else:
        print(f"{searched_name} -> {phonebook[searched_name]}")
