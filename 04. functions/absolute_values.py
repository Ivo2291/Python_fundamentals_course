numbers_list = input().split()
absolute_values_of_numbers = []

for number in numbers_list:
    current_number = abs(float(number))
    absolute_values_of_numbers.append(current_number)

print(absolute_values_of_numbers)
