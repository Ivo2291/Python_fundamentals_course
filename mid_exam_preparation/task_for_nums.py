numbers = list(map(int, input().split()))
average_sum = sum(numbers) / len(numbers)
numbers = [num for num in numbers if num > average_sum]
top_numbers = sorted(numbers, key=lambda x: -x)
final_list = []

for num in top_numbers:
    final_list.append(num)

    if len(final_list) == 5:
        break

if not final_list:
    print("No")

else:
    final_list = list(map(str, final_list))
    print(" ".join(final_list))
