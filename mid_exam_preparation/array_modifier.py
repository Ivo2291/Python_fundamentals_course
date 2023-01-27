numbers = list(map(int, input().split()))
command = input()

while command != "end":
    if command == "decrease":
        numbers = [num - 1 for num in numbers]

    else:
        split_command = command.split()
        current_command = split_command[0]
        first_index = int(split_command[1])
        second_index = int(split_command[2])

        if current_command == "swap":
            numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]

        elif current_command == "multiply":
            numbers[first_index] = numbers[first_index] * numbers[second_index]

    command = input()

numbers = list(map(str, numbers))
modified_list = ", ".join(numbers)
print(modified_list)
