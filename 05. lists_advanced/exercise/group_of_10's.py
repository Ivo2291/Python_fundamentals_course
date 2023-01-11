sequence_of_numbers = [int(number) for number in input().split(", ")]
group_of_numbers = 10
counter = 0

while len(sequence_of_numbers) > counter:
    collected_numbers = []
    for current_number in sequence_of_numbers:
        if group_of_numbers - 10 < current_number <= group_of_numbers:
            collected_numbers.append(current_number)
            counter += 1
    print(f"Group of {group_of_numbers}'s: {collected_numbers}")
    group_of_numbers += 10
