sequence_of_words = input().split()
sequence_of_words = list(map(lambda w: w.lower(), sequence_of_words))
words_dict = {}

for word in sequence_of_words:
    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] += 1

list_of_words = []

for word in words_dict:
    if words_dict[word] % 2 != 0:
        list_of_words.append(word)

print(" ".join(list_of_words))
