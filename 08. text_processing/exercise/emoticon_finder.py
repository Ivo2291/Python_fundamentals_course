text = input()

for char in range(len(text)):
    if text[char] == ":":
        print(text[char] + text[char + 1])
