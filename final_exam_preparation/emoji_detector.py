import re

text = input()
numbers_list = [int(el) for el in text if el.isdigit()]
cool_threshold = 1
emojis_list = []
cool_emojis = []

for num in numbers_list:
    cool_threshold *= num

pattern = r"(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})\1"
matches = re.finditer(pattern, text)

for match in matches:
    current_emoji = match.group()
    emojis_list.append(current_emoji)
    emojis_without_surrounding = match.group("emoji")
    coolness = [ord(el) for el in emojis_without_surrounding]

    if sum(coolness) >= cool_threshold:
        cool_emojis.append(current_emoji)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis_list)} emojis found in the text. The cool ones are:")

for emoji in cool_emojis:
    print(emoji)

# second_solution

# import re
#
# text = input()
# cool_threshold = [int(el) for el in text if el.isdigit()]
# cool_threshold_sum = 1
# cool_emojis = []
# emojis_counter = 0
#
# for num in cool_threshold:
#     cool_threshold_sum *= num
#
# pattern = r"(\*\*|::)([A-Z][a-z]{2,})\1"
# matches = re.finditer(pattern, text)
#
# for match in matches:
#     coolness = sum([ord(el) for el in match.group(2)])
#
#     if coolness > cool_threshold_sum:
#         cool_emojis.append(match.group())
#     emojis_counter += 1
#
# print(f"Cool threshold: {cool_threshold_sum}")
# print(f"{emojis_counter} emojis found in the text. The cool ones are:")
#
# for emoji in cool_emojis:
#     print(emoji)
