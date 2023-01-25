text = input()
index = 0
current_string = ""
final_text = ""

while index < len(text):
    if not text[index].isdigit():
        current_string += text[index]
        index += 1
    else:
        current_digit = ""
        while text[index].isdigit():
            current_digit += text[index]
            index += 1
            if index == len(text):
                break

        final_text += current_string.upper() * int(current_digit)
        current_string = ""

print(f"Unique symbols used: {len(set(final_text))}")
print(final_text)
