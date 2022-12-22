numbers = list(map(int, input().split(", ")))
even_indices_list = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_indices_list.append(i)

print(even_indices_list)
