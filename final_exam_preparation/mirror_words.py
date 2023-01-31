import re

text = input()
mirror_words = []
final_list = []

pattern = r"([#@])(?P<first_word>[A-Za-z]{3,})\1\1(?P<second_word>[A-Za-z]{3,})\1"
matches = [match for match in re.finditer(pattern, text)]

if matches:
    print(f"{len(matches)} word pairs found!")

    for match in matches:
        first_word = match.group("first_word")
        second_word = match.group("second_word")
        reversed_word = reversed(second_word)

        if first_word == "".join(reversed_word):
            mirror_words.append(match.group("first_word"))
            mirror_words.append(match.group("second_word"))
else:
    print("No word pairs found!")

if not mirror_words:
    print("No mirror words!")

else:
    print("The mirror words are:")
    for i in range(1, len(mirror_words), 2):
        final_list.append(mirror_words[i - 1] + " <=> " + mirror_words[i])

    print(", ".join(final_list))

# second_solution

# import re
#
# text = input()
# pattern = r"(#|@)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
# matches = re.finditer(pattern, text)
# match_counter = 0
# mirror_words = []
#
# for match in matches:
#     if match:
#         first_word = match.group(2)
#         second_word = match.group(3)
#         reversed_word = reversed(second_word)
#
#         if first_word == "".join(reversed_word):
#             mirror_words.append(first_word + " <=> " + second_word)
#
#         match_counter += 1
#
# if match_counter != 0:
#     print(f"{match_counter} word pairs found!")
# else:
#     print("No word pairs found!")
#
# if len(mirror_words):
#     print("The mirror words are:")
#     print(", ".join(mirror_words))
#
# else:
#     print("No mirror words!")
