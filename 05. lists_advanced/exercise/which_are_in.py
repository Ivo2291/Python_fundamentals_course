substrings = input().split(", ")
strings = input()
result = [i for i in substrings if i in strings]

print(result)

# second_solution

first_sequence_of_string = input().split(", ")
second_sequence_of_string = input().split(", ")
substrings_list = []

for substring in first_sequence_of_string:
    for string in second_sequence_of_string:
        if substring in string and substring not in substrings_list:
            substrings_list.append(substring)

print(substrings_list)
