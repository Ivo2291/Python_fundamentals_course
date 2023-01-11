sequence_of_numbers = [int(number) for number in input().split()]
sum_of_numbers = 0

while sequence_of_numbers:
    indices_number = int(input())
    if indices_number < 0:
        removed_number = sequence_of_numbers.pop(0)
        sum_of_numbers += int(removed_number)
        sequence_of_numbers.insert(0, sequence_of_numbers[-1])
    elif indices_number >= len(sequence_of_numbers):
        removed_number = sequence_of_numbers.pop(-1)
        sum_of_numbers += int(removed_number)
        sequence_of_numbers.insert(int(sequence_of_numbers[-1]), sequence_of_numbers[0])
    else:
        removed_number = sequence_of_numbers.pop(indices_number)
        sum_of_numbers += removed_number

    for index in range(len(sequence_of_numbers)):
        if removed_number >= sequence_of_numbers[index]:
            sequence_of_numbers[index] += removed_number
        else:
            sequence_of_numbers[index] -= removed_number

print(sum_of_numbers)
