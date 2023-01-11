numbers = list(map(int, input().split(", ")))

positive = [str(num) for num in numbers if num >= 0]
negative = [str(num) for num in numbers if num < 0]
even = [str(num) for num in numbers if num % 2 == 0]
odd = [str(num) for num in numbers if num % 2 != 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")


# second_solution

def positive(nums):
    return [str(num) for num in nums if num >= 0]


def negative(nums):
    return [str(num) for num in nums if num < 0]


def odd(nums):
    return [str(num) for num in nums if num % 2 != 0]


def even(nums):
    return [str(num) for num in nums if num % 2 == 0]


numbers = [int(number) for number in input().split(", ")]

print(f"Positive: {', '.join(positive(numbers))}")
print(f"Negative: {', '.join(negative(numbers))}")
print(f"Even: {', '.join(even(numbers))}")
print(f"Odd: {', '.join(odd(numbers))}")
