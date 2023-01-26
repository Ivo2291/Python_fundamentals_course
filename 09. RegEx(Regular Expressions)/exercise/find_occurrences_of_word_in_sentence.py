import re

text = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"

matches = re.findall(pattern, text, re.I)

print(len(matches))
