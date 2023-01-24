text = input().split()
final_text = ""

for word in text:
    final_text += word * len(word)

print(final_text)
