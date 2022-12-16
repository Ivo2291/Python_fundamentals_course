def sum_numbers(first_num, second_num):
    return first_num + second_num


def subtract(sum_func, third_num):
    return sum_func - third_num


number_one = int(input())
number_two = int(input())
number_three = int(input())

result = subtract(sum_numbers(number_one, number_two), number_three)

print(result)
