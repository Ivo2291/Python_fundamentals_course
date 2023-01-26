import re

text = input()
pattern = r"((\bwww)\.([A-Za-z\d+-]+)\.([a-z\.]+)\b)"
valid_links = []

while text:
    matches = re.finditer(pattern, text)
    for match in matches:
        if match:
            valid_links.append(match.group(1))

    text = input()

for link in valid_links:
    print(link)
