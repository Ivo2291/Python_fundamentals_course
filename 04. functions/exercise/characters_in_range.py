def char_in_range(ch1, ch2):
    for i in range(ord(ch1) + 1, ord(ch2)):
        print(chr(i), end=' ')


char1 = input()
char2 = input()
char_in_range(char1, char2)


# second_solution

def characters_between(a, b):
    char_list = []
    for i in range(ord(a) + 1, ord(b)):
        char_list.append(chr(i))
    return " ".join(char_list)


first_char = input()
second_char = input()

print(characters_between(first_char, second_char))
