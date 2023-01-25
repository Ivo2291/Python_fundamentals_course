text = input()
new_text = ""
current_char = ""

for char in text:
    if current_char != char:
        new_text += char
        current_char = char

print(new_text)
