def calculator(calc_operator, a, b):
    if calc_operator == "multiply":
        return a * b
    elif calc_operator == "divide":
        return int(a / b)
    elif calc_operator == "add":
        return a + b
    elif calc_operator == "subtract":
        return a - b


operator = input()
firs_num = int(input())
second_num = int(input())

print(calculator(operator, firs_num, second_num))
