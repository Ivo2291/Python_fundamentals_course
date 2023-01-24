text = input()
encrypted_text = ""

text = [int(ord(x)) + 3 for x in text]

for digit in text:
    encrypted_text += chr(digit)

print(encrypted_text)
