from string import ascii_lowercase

strings = input().split()
total_sum = 0

for element in strings:
    numbers_in_string = [num for num in element if num.isdigit()]
    result = 0

    for i in range(len(element)):
        if element[i].isalpha():
            index = ascii_lowercase.index(element[i].lower()) + 1

            if i == 0:
                if element[i] == element[i].upper():
                    result += int("".join(numbers_in_string)) / index
                else:
                    result += int("".join(numbers_in_string)) * index

            else:
                if element[i] == element[i].upper():
                    result -= index
                else:
                    result += index

    total_sum += result

print(f"{total_sum:.2f}")
