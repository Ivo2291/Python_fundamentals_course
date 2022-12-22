secret_message = input().split()
deciphered_message = []

for word in secret_message:
    current_word = []
    number_as_string = []

    for current_digit in word:
        if current_digit.isdigit():
            number_as_string.append(current_digit)
        else:
            current_word.append(current_digit)

    number_for_ascii = int("".join(number_as_string))
    current_word.insert(0, chr(number_for_ascii))
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    deciphered_message.append("".join(current_word))

print(" ".join(deciphered_message))


# second_solution

def int_to_chr(word):
    string = list(word)
    num_as_str = []

    while string[0].isdigit():
        num_as_str.append(string[0])
        string.pop(0)

    num = int(''.join(num_as_str))
    string.insert(0, chr(num))
    return ''.join(string)


def switch_letters(word):
    letters = list(word)
    letters[1], letters[-1] = letters[-1], letters[1]
    return ''.join(letters)


print(' '.join([switch_letters(int_to_chr(word)) for word in input().split()]))
