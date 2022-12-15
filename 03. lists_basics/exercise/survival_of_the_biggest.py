import sys

numbers = input().split(" ")
copy_numbers = list(map(int, numbers))
count_of_numbers_to_remove = int(input())

for i in range(count_of_numbers_to_remove):
    current_min_element = min(copy_numbers)
    copy_numbers.remove(current_min_element)
    numbers.remove(str(current_min_element))

print(", ".join(numbers))

# second_solution using sys

list_of_numbers = input().split()
count_to_remove = int(input())
integers_list = []
smallest_number = sys.maxsize

for index in range(len(list_of_numbers)):
    integers_list.append(int(list_of_numbers[index]))

for number in range(count_to_remove):
    smallest_number = sys.maxsize

    for i in integers_list:
        if i < smallest_number:
            smallest_number = i
    if smallest_number in integers_list:
        integers_list.remove(smallest_number)
        list_of_numbers.remove(str(smallest_number))

print(", ".join(list_of_numbers))
