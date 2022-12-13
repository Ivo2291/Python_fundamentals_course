number = int(input())

even = []
odd = []
negative = []
positive = []

for i in range(number):
    current_number = int(input())
    if current_number % 2 == 0:
        even.append(current_number)
    else:
        odd.append(current_number)
    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

command = input()

print(eval(command))

# second_solution

number = int(input())
numbers_filter = []
list_of_current_numbers = []

for num in range(number):
    current_number = int(input())
    list_of_current_numbers.append(current_number)

command = input()

if command == "even":
    for number in list_of_current_numbers:
        if number % 2 == 0:
            numbers_filter.append(number)
elif command == "odd":
    for number in list_of_current_numbers:
        if number % 2 != 0:
            numbers_filter.append(number)
elif command == "negative":
    for number in list_of_current_numbers:
        if number < 0:
            numbers_filter.append(number)
elif command == "positive":
    for number in list_of_current_numbers:
        if number >= 0:
            numbers_filter.append(number)

print(numbers_filter)
