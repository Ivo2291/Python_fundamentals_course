def smallest_number(a, b, c):
    print((min(a, b, c)))


first_number, second_number, third_number = int(input()), int(input()), int(input())
smallest_number(first_number, second_number, third_number)


# second_solution


def find_the_smallest(first_num, second_num, third_num):
    if first_num < second_num and first_num < third_num:
        return first_num
    elif second_num < first_num and second_num < third_num:
        return second_num
    else:
        return third_num


number_one = int(input())
number_two = int(input())
number_three = int(input())

print(find_the_smallest(number_one, number_two, number_three))
