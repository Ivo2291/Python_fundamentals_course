strings = input()
count_of_beggars = int(input())

integers_list = strings.split(", ")
earns = []

for i in range(count_of_beggars):
    earns.append(int(0))

while integers_list:
    for i in range(count_of_beggars):
        earns[i] += int(integers_list[0])
        integers_list.remove(integers_list[0])
        if not integers_list:
            break

print(earns)

# second_solution

numbers_list = list(map(int, input().split(", ")))
count_of_beggars = int(input())

sum_counter = 0
index_counter = 0
beggars_sum_list = []

while index_counter < count_of_beggars:
    for number in range(index_counter, len(numbers_list), count_of_beggars):
        sum_counter += numbers_list[number]
    beggars_sum_list.append(sum_counter)
    sum_counter = 0
    index_counter += 1

print(beggars_sum_list)
