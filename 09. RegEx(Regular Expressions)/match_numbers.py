import re
numbers_as_string = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

matches = re.finditer(pattern, numbers_as_string)

for match in matches:
    if match:
        print(match.group(), end=" ")
