factor = int(input())
count = int(input())
numbers_list = []

for number in range(1, count + 1):
    numbers_list.append(factor * number)

print(numbers_list)
