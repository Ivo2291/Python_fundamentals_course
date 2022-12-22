# with list comprehension
text = input()
vowels = ['a', 'o', 'u', 'e', 'happiness']
no_vowels_list = [letter for letter in text if letter not in vowels]

print("".join(no_vowels_list))


# without list comprehension
text = input()
vowels = ['a', 'o', 'u', 'e', 'happiness']
no_vowels_list = []

for letter in text:
    if letter not in vowels:
        no_vowels_list.append(letter)

print("".join(no_vowels_list))
