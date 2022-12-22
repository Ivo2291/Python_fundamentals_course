to_do_list = []
for i in range(11):
    to_do_list.append("")

command = input()

while command != "End":
    current_command = command.split("-")
    importance = int(current_command[0])
    note = current_command[1]
    to_do_list[importance] = note

    command = input()

final_to_do_list = [task for task in to_do_list if task != ""]

print(final_to_do_list)
