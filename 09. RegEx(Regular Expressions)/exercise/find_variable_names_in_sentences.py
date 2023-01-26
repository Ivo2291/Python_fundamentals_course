import re

text = input()
pattern = r"\b_([a-zA-Z\d?]+)\b"

matches = re.findall(pattern, text)

print(",".join(matches))
