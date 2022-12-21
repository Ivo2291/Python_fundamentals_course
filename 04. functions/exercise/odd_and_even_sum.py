def odd_and_even_digits_sum(number):
    odd_sum = 0
    even_sum = 0
    for num in number:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


current_number = map(int, list(input()))
odd_and_even_digits_sum(current_number)


# second_solution


def get_odd_and_even_sum(number):
    sum_of_even_numbers = 0
    sum_of_odd_numbers = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even_numbers += int(digit)
        else:
            sum_of_odd_numbers += int(digit)

    return sum_of_even_numbers, sum_of_odd_numbers


number_as_string = input()
evens_sum, odds_sum = get_odd_and_even_sum(number_as_string)

print(f"Odd sum = {odds_sum}, Even sum = {evens_sum}")
