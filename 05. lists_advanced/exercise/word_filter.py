text = input().split()
text = [word for word in text if len(word) % 2 == 0]

print("\n".join(text))

# second_solution

text = input().split()
filtered_text = list(filter(lambda word: len(word) % 2 == 0, text))

print("\n".join(filtered_text))
