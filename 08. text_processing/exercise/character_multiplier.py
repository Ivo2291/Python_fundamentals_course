first_string, second_string = input().split()
total_sum = 0

if len(first_string) > len(second_string):
    for i in range(len(first_string)):
        if i < len(second_string):
            total_sum += ord(first_string[i]) * ord(second_string[i])
        else:
            total_sum += ord(first_string[i])
else:
    for i in range(len(second_string)):
        if i < len(first_string):
            total_sum += ord(second_string[i]) * ord(first_string[i])
        else:
            total_sum += ord(second_string[i])

print(total_sum)
