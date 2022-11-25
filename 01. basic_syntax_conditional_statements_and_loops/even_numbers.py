number = int(input())
all_numbers_are_even = True

for nums in range(number):
    current_number = int(input())

    if current_number % 2 == 0:
        continue
    else:
        all_numbers_are_even = False
        print(f"{current_number} is odd!")
        break

if all_numbers_are_even:
    print("All numbers_as_integers are even.")
