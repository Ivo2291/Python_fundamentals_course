number = int(input())

positive_numbers = []
negative_numbers = []
count_of_positives = 0
sum_of_negatives = 0

for num in range(number):
    current_number = int(input())
    if current_number >= 0:
        count_of_positives += 1
        positive_numbers.append(current_number)
    else:
        sum_of_negatives += current_number
        negative_numbers.append(current_number)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {count_of_positives}")
print(f"Sum of negatives: {sum_of_negatives}")

# second_solution

number = int(input())

positive_numbers = []
negative_numbers = []

for num in range(number):
    current_number = int(input())
    if current_number >= 0:
        positive_numbers.append(current_number)
    else:
        negative_numbers.append(current_number)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")
