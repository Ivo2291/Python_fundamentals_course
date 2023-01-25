text = input()
strength = 0
new_text = ""

for index in range(len(text)):

    if text[index] == ">":
        strength += int(text[index + 1])
        new_text += text[index]

    elif text[index] != ">" and strength > 0:
        strength -= 1

    else:
        new_text += text[index]

print(new_text)
