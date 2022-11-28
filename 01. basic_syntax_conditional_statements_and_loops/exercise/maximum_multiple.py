divisor = int(input())
boundary = int(input())

result = int(boundary / divisor) * divisor

print(result)

# second_solution

divisor = int(input())
boundary = int(input())
maximum_multiply = 0

for number in range(divisor, boundary + 1):
    if number % divisor == 0 and number <= boundary and number != 0:
        maximum_multiply = number

print(maximum_multiply)
