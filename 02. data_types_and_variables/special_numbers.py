number = int(input())

for num in range(1, number + 1):
    sum_of_digits = 0
    digit = num

    while digit > 0:
        sum_of_digits += digit % 10
        digit = int(digit / 10)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
