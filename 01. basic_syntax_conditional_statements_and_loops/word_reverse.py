word = input()
reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print(reversed_word)

# second_solution

for idx in range(len(word) - 1, - 1, - 1):
    print(word[idx], end="")

# third_solution

print()

reversed_w = ''.join(reversed(word))
print(reversed_w)
