def perfect_number(number):
    total_sum = 0
    for num in range(1, number):
        if number % num == 0:
            total_sum += num
    if total_sum == number:
        return "We have a perfect old_version!"
    return "It's not so perfect."


given_number = int(input())
print(perfect_number(given_number))
