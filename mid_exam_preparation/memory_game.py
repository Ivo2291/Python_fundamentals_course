elements = input().split()
temp_list = []
turns = 0
command = input()

while command != "end":
    turns += 1
    current_command = command.split()
    first_index = int(current_command[0])
    second_index = int(current_command[1])

    if first_index != second_index and 0 <= first_index < len(elements) \
            and 0 <= second_index < len(elements):

        if elements[first_index] == elements[second_index]:
            print(f"Congrats! You have found matching elements - {elements[first_index]}!")
            temp_list = [element for element in elements if element != elements[first_index]]
            elements = temp_list

        else:
            print("Try again!")

        if len(elements) == 0:
            print(f"You have won in {turns} turns!")
            break

    else:
        elements.insert(len(elements) // 2, f"-{str(turns)}a")
        elements.insert(len(elements) // 2, f"-{str(turns)}a")
        print("Invalid input! Adding additional elements to the board")

    command = input()

if command == "end":
    print("Sorry you lose :(")
    print(" ".join(elements))
