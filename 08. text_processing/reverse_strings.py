word = input()

while word != "end":
    reversed_word = reversed(word)
    print(f"{word} = {''.join(reversed_word)}")
    word = input()
