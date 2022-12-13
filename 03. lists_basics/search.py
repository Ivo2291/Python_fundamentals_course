number = int(input())
word = input()

strings_list = []
filtered_list = []

for num in range(number):
    some_string = input()
    strings_list.append(some_string)
    if word in some_string:
        filtered_list.append(some_string)

print(strings_list)
print(filtered_list)
