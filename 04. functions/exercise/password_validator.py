def length_of_password(string):
    if 6 <= len(string) <= 10:
        return True
    print("Password must be between 6 and 10 characters")


def letters_and_digits(letters_or_digits):
    if letters_or_digits.isalnum():
        return True
    print("Password must consist only of letters and digits")


def digits_validator(digits):
    counter = 0
    for symbol in digits:
        if symbol.isdigit():
            counter += 1
    if counter >= 2:
        return True
    print("Password must have at least 2 digits")


password = input()
result = [length_of_password(password), letters_and_digits(password), digits_validator(password)]

if all(result):
    print("Password is valid")
