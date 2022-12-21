def factorial_func(num):
    return 1 if num == 0 or num == 1 else num * factorial_func(num - 1)


num1 = int(input())
num2 = int(input())
result = factorial_func(num1) / factorial_func(num2)
print(f"{result:.2f}")


# second_solution

def factorial(number):
    for num in range(1, number):
        number *= num
    return number


first_number = int(input())
second_number = int(input())
first_result = factorial(first_number)
second_result = factorial(second_number)
final_result = first_result / second_result
print(f"{final_result:.2f}")
